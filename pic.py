from flask import Flask,request,Response
import json
app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_flask():
    from PIL import Image
    import urllib.request
    data = request.get_json()

    rsp = urllib.request.urlopen(data.get("title").replace("132","0"))
    img = rsp.read()
    path = "data/user_pic/{}.jpg".format(data.get("value"))
    with open(path,'wb') as f:
        f.write(img)
    guoqi_path = 'https://656e-env01-5gyp95fi9a152dfa-1307030481.tcb.qcloud.la/deco_pic/guoqi.png?sign=9d314c1cfadddc481dad2561c10750a4&t=1635777402'
    rsp2 = urllib.request.urlopen(guoqi_path)
    img2 = rsp2.read()
    path2 = "data/local_pic/guoqi.png"
    with open(path2,'wb') as f:
        f.write(img2)
    s_avatar = Image.open(path).convert("RGBA")
    s_banner = Image.open('data/local_pic/guoqi.png').convert("RGBA").resize(s_avatar.size)

    # 将五星红旗图片设置透明渐变
    w, h = s_banner.size
    for i in range(w):
        for j in range(h):
            alpha = int(255-(i*(255/int(w*0.8)))) if int(255-(i*(255/int(w*0.8)))) > 0 else 0
            s_banner.putpixel((i, j), s_banner.getpixel((i, j))[:-1] + (alpha, ))

    # 将五星红旗图片粘贴到头像图片并保存
    s_avatar.paste(s_banner, (0,0), s_banner)

    print("hello")
    s_avatar.save('data/logs/{}.png'.format(data.get("value")))
    print(data)
    print(type(data))
    return "https://background-1333966-1307030481.ap-shanghai.run.tcloudbase.com:15000/code/data/logs/{}.png".format(data.get("value"))

@app.route("/data/logs/<imageId>.png")
def get_frame(imageId):
    # 图片上传保存的路径
    with open(r'data/logs/{}.png'.format(imageId), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/png")
        return resp



if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=15000)

