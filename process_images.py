from PIL import Image

def remove_white_background(input_path, output_path, threshold=240):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Check if pixel is close to white
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                newData.append((255, 255, 255, 0))  # Transparent
            else:
                newData.append(item)
        
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Processed {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

files = [
    ("hero-bowl-white.png", "hero-bowl.png"),
    ("leaf-1-white.png", "leaf-top-left.png"),
    ("leaf-2-white.png", "leaf-bottom-right.png"),
    ("sushi-hand.png", "sushi-hand-proc.png") # original might be named sushi-hand.png, save to new
]

# Note: for sushi-hand.png, if it was already replaced by a transparent one in step 44, 
# I might be using the checkerboard one. 
# Step 24 copy was the white-bg one. Step 44 copy was the transparent-checkerboard one.
# White-bg one was step 14. 
# I should try to use the white-bg one if possible. 
# The one at 'sushi-hand.png' right now is likely the Step 44 one (transparent checkerboard).
# I need to restore the white one first if I want to use this script effectively, 
# OR I just try running it on what I have. If it has alpha channel already, this script might just pass it through or mess it up.
# Let's assume I need to fetch the white one again.
# White one path: /Users/newtonbrian/.gemini/antigravity/brain/59a9838a-e848-45c5-9732-caa5928e8265/sushi_hand_1769961147037.png

# Re-list with absolute original paths where possible for safety
files_abs = [
    ("hero-bowl-white.png", "hero-bowl.png"),
    ("leaf-1-white.png", "leaf-top-left.png"),
    ("leaf-2-white.png", "leaf-bottom-right.png"),
    ("/Users/newtonbrian/.gemini/antigravity/brain/59a9838a-e848-45c5-9732-caa5928e8265/sushi_hand_1769961147037.png", "sushi-hand.png")
]

for inp, out in files_abs:
    remove_white_background(inp, out)
