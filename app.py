from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"受信データ: {data}") 
    content = data.get('content', {}).get('text', '')
    print(f"受信テキスト: {content}") 
    if content.count('-') >= 3:
        channel_id = content.strip()
        link = f"https://line.worksmobile.com/message/send?version=26&channelId={channel_id}"
        reply_text = f"以下のリンクからトークルームにアクセスできます：\n{link}"
    else:
        reply_text = "チャンネルIDの形式が正しくありません。"

    return jsonify({
    "text": reply_text
})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
