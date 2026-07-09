from fastapi import APIRouter, UploadFile, File


router = APIRouter()


@router.post("/upload-video")
async def upload_video(
    file: UploadFile = File(...)
):

    return {
        "filename": file.filename,
        "message": "Video received"
    }