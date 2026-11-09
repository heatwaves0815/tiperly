from PIL import Image, ImageDraw, ImageFont

scale = 3
canvas = Image.new("RGBA", (256 * scale, 256 * scale), (0, 0, 0, 0))
d = ImageDraw.Draw(canvas)
px = lambda n: int(n * scale)
d.rounded_rectangle((px(8), px(8), px(248), px(248)), radius=px(70), fill="#243d35")
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", px(158))
box = d.textbbox((0, 0), "t", font=font)
d.text((px(50), px(26) - box[1]), "t", font=font, fill="#f6f7f1", stroke_width=0)
d.ellipse((px(174), px(54), px(205), px(85)), fill="#c3e582")
canvas.resize((256, 256), Image.Resampling.LANCZOS).save("icon.ico", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
