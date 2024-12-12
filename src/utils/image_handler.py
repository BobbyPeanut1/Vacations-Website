from pathlib import Path
from flask import current_app
from uuid import uuid4


class ImageHandler:

    @staticmethod
    def save_image(image, old_image_is_none = True):
        if not image:
            return None
        suffx = Path(image.filename).suffix 
        image_name = str(uuid4()) + suffx 
        image_path = ImageHandler.get_image_path(image_name, old_image_is_none) 
        image.save(image_path) 
        return image_name

    @staticmethod
    def get_image_path(image_name, old_image_is_none = True):
        image_path = Path(current_app.root_path) / f"static/images/vacation_images/{image_name}"

        if not image_path.exists() and old_image_is_none:
            image_path = Path(current_app.root_path) / "static/images/vacation_images/No-Image-Placeholder.png"

        return image_path




    @staticmethod
    def update_image(old_image_name, new_image):
        if not new_image.filename:
            return old_image_name

        image_name = ImageHandler.save_image(new_image, False) # false is entered to not make every updated image replace the placeholder
        ImageHandler.delete_image(old_image_name)
        return image_name
    
    @staticmethod
    def delete_image(image_name):
        if not image_name:
            return
        
        if image_name == "No-Image-Placeholder.png":
            return
        
        image_path = Path(current_app.root_path) / f"static/images/vacation_images/{image_name}"
        image_path.unlink(missing_ok = True)