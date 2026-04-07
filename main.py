import cv2

def convert_to_sketch(image_path, output_path):
    # 1. Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not find image. Check the path!")
        return

    # 2. Convert to Grayscale
    # A sketch doesn't have color, so we strip it out first.
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Invert the Grayscale Image
    # This helps us identify the edges and contours later.
    inverted_gray = cv2.bitwise_not(gray_img)

    # 4. Apply a Gaussian Blur
    # This is the secret sauce. The larger the kernel size (e.g., 21x21), 
    # the softer and more realistic the sketch shading will look. 
    # You can tweak the (21, 21) values to change the sketch style.
    blurred_img = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

    # 5. Invert the Blurred Image
    inverted_blurred = cv2.bitwise_not(blurred_img)

    # 6. Create the Sketch (Color Dodge Blend)
    # We divide the grayscale image by the inverted blurred image. 
    # This brightens the background and leaves the edges dark, creating a pencil effect.
    sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)

    # 7. Save the beautiful result!
    cv2.imwrite(output_path, sketch)
    print(f"Success! Sketch saved to {output_path}")

# --- Run the function ---
# Replace with your actual image file names
convert_to_sketch("vijay.jpg", "vijay_sketch.jpg")

def convert_to_sketch(image_path, output_path):
    # 1. Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not find image. Check the path!")
        return

    # 2. Convert to Grayscale
    # A sketch doesn't have color, so we strip it out first.
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Invert the Grayscale Image
    # This helps us identify the edges and contours later.
    inverted_gray = cv2.bitwise_not(gray_img)

    # 4. Apply a Gaussian Blur
    # This is the secret sauce. The larger the kernel size (e.g., 21x21), 
    # the softer and more realistic the sketch shading will look. 
    # You can tweak the (21, 21) values to change the sketch style.
    blurred_img = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

    # 5. Invert the Blurred Image
    inverted_blurred = cv2.bitwise_not(blurred_img)

    # 6. Create the Sketch (Color Dodge Blend)
    # We divide the grayscale image by the inverted blurred image. 
    # This brightens the background and leaves the edges dark, creating a pencil effect.
    sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)

    # 7. Save the beautiful result!
    cv2.imwrite(output_path, sketch)
    print(f"Success! Sketch saved to {output_path}")

# --- Run the function ---
# Replace with your actual image file names
convert_to_sketch("vijay.jpg", "vijay_sketch.jpg")