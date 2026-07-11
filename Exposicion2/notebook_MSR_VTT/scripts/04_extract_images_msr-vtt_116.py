from pathlib import Path

import cv2
import pandas as pd
from tqdm import tqdm


PROJECT_ROOT = Path(__file__).resolve().parent.parent


VIDEO_DIR = PROJECT_ROOT / "data" / "msr-vtt" / "videos"

IMAGES_DIR = PROJECT_ROOT / "data" / "raw"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

METADATA_CSV = OUTPUT_DIR / "sports_msr-vtt_metadata.csv"

OUTPUT_CSV = OUTPUT_DIR / "msr-vtt_images.csv"



def extract_center_frame(video_path, output_dir):

    cap = cv2.VideoCapture(
        str(video_path)
    )


    if not cap.isOpened():

        print(
            f"[WARN] No se pudo abrir: {video_path}"
        )

        return None


    total_frames = int(
        cap.get(
            cv2.CAP_PROP_FRAME_COUNT
        )
    )


    if total_frames <= 0:

        cap.release()

        return None


    # Tomar frame central del video
    frame_number = total_frames // 2


    cap.set(
        cv2.CAP_PROP_POS_FRAMES,
        frame_number
    )


    success, frame = cap.read()


    cap.release()


    if not success:

        return None



    video_id = video_path.stem


    image_path = (
        output_dir /
        f"{video_id}.jpg"
    )


    cv2.imwrite(
        str(image_path),
        frame
    )


    return {
        "video_id": video_id,
        "image_path": str(
            image_path.resolve()
        )
    }




def main():

    print("Proyecto:")
    print(PROJECT_ROOT)

    print()


    print("Leyendo metadata:")
    print(METADATA_CSV)


    metadata = pd.read_csv(
        METADATA_CSV
    )


    print()

    print(
        "Videos encontrados:",
        len(metadata)
    )


    IMAGES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    records = []


    for _, row in tqdm(
        metadata.iterrows(),
        total=len(metadata)
    ):


        video_id = row["video_id"]

        caption = row["caption"]


        video_path = (
            VIDEO_DIR /
            f"{video_id}.mp4"
        )


        if not video_path.exists():

            print(
                f"[WARN] No existe: {video_path}"
            )

            continue



        image = extract_center_frame(
            video_path,
            IMAGES_DIR
        )


        if image is not None:


            image["video_path"] = str(
                video_path.resolve()
            )


            image["caption"] = caption


            records.append(
                image
            )



    df = pd.DataFrame(
        records
    )


    df.to_csv(
        OUTPUT_CSV,
        index=False
    )


    print()

    print(
        "Imágenes generadas:",
        len(df)
    )


    print(
        "CSV generado:",
        OUTPUT_CSV
    )


    print()

    print(
        df.head()
    )



if __name__ == "__main__":
    main()