from __future__ import annotations

import argparse
import json
import os
from io import BytesIO
from pathlib import Path

import pandas as pd
from PIL import Image
from datasets import load_dataset, DownloadConfig


def extract_captions(item) -> list[str]:
    for key in ['caption', 'captions', 'sentence', 'sentences', 'text']:
        if key in item:
            value = item[key]
            break
    else:
        value = ''

    if isinstance(value, str):
        captions = [value]
    elif isinstance(value, dict):
        captions = list(value.values())
    elif isinstance(value, (list, tuple)):
        captions = list(value)
    else:
        captions = [str(value)]

    captions = [str(c).strip() for c in captions if str(c).strip()]
    return captions or ['']


def pil_image_from_item(item) -> Image.Image:
    image = item.get('image', None)
    if isinstance(image, Image.Image):
        return image.convert('RGB')
    if isinstance(image, dict):
        if image.get('bytes') is not None:
            return Image.open(BytesIO(image['bytes'])).convert('RGB')
        if image.get('path') is not None:
            return Image.open(image['path']).convert('RGB')
    if isinstance(image, (str, os.PathLike)):
        return Image.open(image).convert('RGB')
    try:
        return Image.fromarray(image).convert('RGB')
    except Exception as exc:
        raise ValueError(f'Could not convert dataset image to PIL: {type(exc).__name__}: {exc}') from exc


def safe_load_hf_dataset(dataset_id: str, split: str):
    try:
        return load_dataset(dataset_id, split=split, download_config=DownloadConfig(max_retries=3))
    except TypeError:
        # Compatibility with older versions of datasets.
        return load_dataset(dataset_id, split=split)


def prepare_subset(output_root: Path, dataset_id: str, split: str, limit: int, random_state: int) -> Path:
    output_root = Path(output_root)
    image_dir = output_root / 'images'
    image_dir.mkdir(parents=True, exist_ok=True)

    ds = safe_load_hf_dataset(dataset_id, split)
    n = min(int(limit), len(ds))
    if n < 100:
        raise RuntimeError(f'The selected backend returned only {n} records; use at least 100 for the expanded evaluation.')

    try:
        subset = ds.shuffle(seed=random_state).select(range(n))
    except Exception:
        subset = ds.select(range(n))

    rows = []
    for idx, item in enumerate(subset):
        image = pil_image_from_item(item)
        source_filename = str(item.get('filename', f'{split}_{idx:05d}.jpg'))
        suffix = Path(source_filename).suffix.lower() or '.jpg'
        fname = f'{split}_{idx:05d}{suffix}'
        image.save(image_dir / fname, quality=95)
        captions = extract_captions(item)
        rows.append({
            'image_id': f'{split}_{idx:05d}',
            'source_image_id': str(item.get('img_id', item.get('image_id', idx))),
            'source_filename': source_filename,
            'filename': fname,
            'filepath': str(Path('data') / output_root.name / 'images' / fname),
            'split': split,
            'caption': captions[0],
            'label': '',
            'all_captions_json': json.dumps(captions, ensure_ascii=False),
            'hf_dataset_id': dataset_id,
        })

    out_csv = output_root / f'{split}.csv'
    pd.DataFrame(rows).to_csv(out_csv, index=False)
    return out_csv


def main() -> None:
    parser = argparse.ArgumentParser(description='Prepare a 100-500 image-caption subset for MCC225 Semana 5.')
    parser.add_argument('--output-root', required=True)
    parser.add_argument('--dataset-id', default='Vishva007/Flickr-Dataset-1k', help='Recommended: Vishva007/Flickr-Dataset-1k')
    parser.add_argument('--split', default='train')
    parser.add_argument('--limit', type=int, default=300)
    parser.add_argument('--random-state', type=int, default=42)
    args = parser.parse_args()

    out_csv = prepare_subset(
        output_root=Path(args.output_root),
        dataset_id=args.dataset_id,
        split=args.split,
        limit=args.limit,
        random_state=args.random_state,
    )
    print('Saved', out_csv)
    print('Dataset:', args.dataset_id)
    print('Split:', args.split)
    print('Limit:', args.limit)


if __name__ == '__main__':
    main()
