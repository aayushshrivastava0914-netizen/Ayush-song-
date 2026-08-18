from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Meri Mehbooba 🎵</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    background:
        radial-gradient(circle at top, #402060, #090914 55%, #000);
    color: white;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.card {
    width: 92%;
    max-width: 500px;
    padding: 30px 22px;
    text-align: center;
    border-radius: 28px;
    background: rgba(20,20,35,.82);
    backdrop-filter: blur(15px);
    box-shadow: 0 0 50px rgba(170,80,255,.25);
}

.cover {
    width: 170px;
    height: 170px;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(135deg,#ff4ecd,#7040ff);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 65px;
    box-shadow: 0 0 35px #b84cff;
    animation: rotate 8s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

h1 {
    margin: 22px 0 5px;
    font-size: 27px;
}

.subtitle {
    color: #aaa;
    margin-bottom: 25px;
}

.lyrics {
    min-height: 120px;
    margin: 20px 0;
    padding: 20px;
    border-radius: 18px;
    background: rgba(255,255,255,.06);
    display: flex;
    align-items: center;
    justify-content: center;
}

.lyric {
    font-size: 21px;
    font-weight: bold;
    color: #fff;
    text-shadow: 0 0 15px #c85cff;
}

audio {
    width: 100%;
}

.visualizer {
    display: flex;
    height: 45px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    margin: 20px 0;
}

.bar {
    width: 6px;
    height: 15px;
    border-radius: 10px;
    background: #d05cff;
    animation: wave .7s infinite alternate;
}

.bar:nth-child(2){animation-delay:.1s}
.bar:nth-child(3){animation-delay:.2s}
.bar:nth-child(4){animation-delay:.3s}
.bar:nth-child(5){animation-delay:.4s}
.bar:nth-child(6){animation-delay:.5s}
.bar:nth-child(7){animation-delay:.6s}

@keyframes wave {
    from {height: 8px}
    to {height: 42px}
}
</style>
</head>

<body>

<div class="card">

    <div class="cover">🎵</div>

    <h1>Meri Mehbooba</h1>
    <div class="subtitle">♪ Now Playing ♪</div>

    <div class="visualizer">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
    </div>

    <div class="lyrics">
        <div class="lyric" id="lyric">
            🎶 Song Playing 🎶
        </div>
    </div>

    <audio id="audio" controls>
        <source src="/static/song.mp3" type="audio/mpeg">
    </audio>

</div>

<script>
const audio = document.getElementById("audio");
const lyric = document.getElementById("lyric");

/*
  Yahan apne lyrics ki lines daal sakte ho.
  time = song ke seconds.
*/
const lyrics = [
    {time: 0, text: "🎶 Song Playing 🎶"},
    {time: 10, text: "✨ Meri Mehbooba ✨"},
    {time: 20, text: "❤️ Music continues..."},
    {time: 30, text: "🎵 Enjoy the song 🎵"}
];

audio.addEventListener("timeupdate", () => {
    let current = lyrics[0];

    for (const line of lyrics) {
        if (audio.currentTime >= line.time) {
            current = line;
        }
    }

    lyric.innerText = current.text;
});
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
