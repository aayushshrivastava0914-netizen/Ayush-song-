from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="hi">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Meri Mehbooba 🎵</title>

<style>

/* =========================
   BASIC
========================= */

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    min-height: 100vh;

    padding: 20px 0;

    display: flex;

    justify-content: center;

    align-items: center;

    overflow-x: hidden;

    font-family: Arial, sans-serif;

    color: white;

    background:
        radial-gradient(
            circle at 20% 10%,
            #45106b 0%,
            transparent 35%
        ),

        radial-gradient(
            circle at 90% 90%,
            #062b66 0%,
            transparent 35%
        ),

        #020208;
}


/* =========================
   BACKGROUND LIGHTS
========================= */

body::before,
body::after {

    content: "";

    position: fixed;

    width: 240px;
    height: 240px;

    border-radius: 50%;

    filter: blur(80px);

    opacity: .35;

    z-index: -1;

    animation:
        floatingLight 6s
        ease-in-out
        infinite
        alternate;
}

body::before {

    background: #ff00dd;

    top: -100px;
    left: -80px;
}

body::after {

    background: #0066ff;

    right: -90px;
    bottom: -90px;

    animation-delay: 2s;
}


@keyframes floatingLight {

    from {
        transform: translate(0, 0);
    }

    to {
        transform: translate(45px, 30px);
    }
}


/* =========================
   MAIN CONTAINER
========================= */

.container {

    width: 94%;

    max-width: 720px;

}


/* =========================
   TITLE
========================= */

.heading {

    text-align: center;

    margin-bottom: 18px;

}

.heading h1 {

    margin: 0;

    font-size:
        clamp(26px, 7vw, 40px);

    color: white;

    text-shadow:

        0 0 5px white,

        0 0 12px #ff00dd,

        0 0 25px #ff00dd,

        0 0 50px #7a00ff;

}

.heading p {

    margin: 8px 0 0;

    color: #aaa;

    font-size: 13px;

}


/* =========================
   MONITOR BODY
========================= */

.monitor {

    padding: 11px;

    background:
        linear-gradient(
            145deg,
            #292933,
            #09090e
        );

    border-radius: 20px;

    border: 2px solid #353540;

    box-shadow:

        0 0 8px #00eaff,

        0 0 25px #00eaff,

        0 0 55px
        rgba(0,180,255,.35),

        0 20px 60px
        rgba(0,0,0,.8);

}


/* =========================
   NEON SCREEN
========================= */

.screen {

    position: relative;

    min-height: 320px;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    overflow: hidden;

    border-radius: 10px;

    background:

        radial-gradient(
            circle at center,
            #092536 0%,
            #040b13 45%,
            #010205 100%
        );

    border: 3px solid #00eaff;

    box-shadow:

        inset 0 0 20px #00eaff,

        inset 0 0 55px #004cff,

        0 0 5px #00eaff,

        0 0 15px #00eaff,

        0 0 35px #00eaff,

        0 0 70px #0055ff;

}


/* Scan lines */

.screen::before {

    content: "";

    position: absolute;

    inset: 0;

    background:

        repeating-linear-gradient(
            0deg,
            transparent 0px,
            transparent 3px,
            rgba(255,255,255,.025) 4px
        );

    pointer-events: none;

}


/* Moving scan light */

.screen::after {

    content: "";

    position: absolute;

    width: 100%;

    height: 2px;

    left: 0;

    top: -5px;

    background: #00eaff;

    box-shadow:

        0 0 10px #00eaff,

        0 0 25px #00eaff;

    opacity: .7;

    animation:
        scanLine 4s
        linear
        infinite;

}


@keyframes scanLine {

    from {
        top: -5px;
    }

    to {
        top: 100%;
    }

}


/* =========================
   LYRICS
========================= */

#lyrics {

    position: relative;

    z-index: 5;

    width: 90%;

    padding: 20px;

    font-size:
        clamp(24px, 6vw, 43px);

    font-weight: 800;

    line-height: 1.35;

    color: white;

    text-shadow:

        0 0 4px #fff,

        0 0 10px #00eaff,

        0 0 20px #00eaff,

        0 0 35px #008cff,

        0 0 60px #0066ff;

    animation:

        neonPulse
        1.5s
        ease-in-out
        infinite
        alternate,

        lyricIn
        .5s
        ease;

}


@keyframes neonPulse {

    from {

        opacity: .78;

        text-shadow:

            0 0 4px #fff,

            0 0 8px #00eaff,

            0 0 18px #00eaff,

            0 0 30px #008cff;

    }

    to {

        opacity: 1;

        text-shadow:

            0 0 5px #fff,

            0 0 15px #00eaff,

            0 0 30px #00eaff,

            0 0 50px #008cff,

            0 0 75px #0066ff;

    }

}


@keyframes lyricIn {

    from {

        opacity: 0;

        transform:
            scale(.8)
            translateY(18px);

    }

    to {

        opacity: 1;

        transform:
            scale(1)
            translateY(0);

    }

}


/* =========================
   CURSOR
========================= */

.cursor {

    display: inline-block;

    width: 7px;

    height: 38px;

    margin-left: 8px;

    vertical-align: middle;

    background: #00eaff;

    box-shadow:

        0 0 8px #00eaff,

        0 0 20px #00eaff;

    animation:
        blink .7s infinite;

}


@keyframes blink {

    0%, 45% {
        opacity: 1;
    }

    46%, 100% {
        opacity: 0;
    }

}


/* =========================
   MONITOR STAND
========================= */

.stand {

    width: 120px;

    height: 22px;

    margin: 0 auto;

    background: #24242c;

    border-radius:
        0 0 12px 12px;

}


.base {

    width: 210px;

    height: 12px;

    margin: 0 auto 20px;

    background: #292932;

    border-radius: 20px;

}


/* =========================
   PLAYER
========================= */

.player {

    padding: 20px;

    border-radius: 22px;

    background:
        rgba(10,10,17,.90);

    border:
        1px solid #292936;

    box-shadow:

        0 0 25px
        rgba(170,0,255,.25),

        0 15px 40px
        rgba(0,0,0,.7);

}


.song-title {

    text-align: center;

    font-size: 19px;

    font-weight: bold;

    margin-bottom: 15px;

    color: white;

    text-shadow:

        0 0 8px #ff00dd,

        0 0 18px #a000ff;

}


/* =========================
   VISUALIZER
========================= */

.visualizer {

    height: 55px;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 5px;

    margin-bottom: 15px;

}


.bar {

    width: 6px;

    height: 9px;

    border-radius: 10px;

    background: #ff00dd;

    box-shadow:

        0 0 8px #ff00dd,

        0 0 18px #ff00dd;

    animation:

        wave .55s
        ease-in-out
        infinite
        alternate,

        rgb 3s
        linear
        infinite;

    animation-play-state:
        paused;

}


.playing .bar {

    animation-play-state:
        running;

}


.bar:nth-child(2) {
    animation-delay: .1s;
}

.bar:nth-child(3) {
    animation-delay: .2s;
}

.bar:nth-child(4) {
    animation-delay: .3s;
}

.bar:nth-child(5) {
    animation-delay: .4s;
}

.bar:nth-child(6) {
    animation-delay: .5s;
}

.bar:nth-child(7) {
    animation-delay: .6s;
}


@keyframes wave {

    from {
        height: 8px;
    }

    to {
        height: 45px;
    }

}


@keyframes rgb {

    0% {
        filter:
            hue-rotate(0deg);
    }

    100% {
        filter:
            hue-rotate(360deg);
    }

}


/* =========================
   AUDIO
========================= */

audio {

    width: 100%;

}


/* =========================
   MOBILE
========================= */

@media (max-width: 500px) {

    .screen {

        min-height: 260px;

    }

    .monitor {

        padding: 7px;

    }

    #lyrics {

        font-size: 27px;

    }

    .player {

        padding: 16px;

    }

}

</style>

</head>


<body>


<div class="container">


<!-- TITLE -->

<div class="heading">

    <h1>
        🎵 MERI MEHBOOBA
    </h1>

    <p>
        ♪ NEON MUSIC PLAYER ♪
    </p>

</div>


<!-- MONITOR -->

<div class="monitor">

    <div class="screen">

        <div id="lyrics">

            🎵 PLAY SONG 🎵

            <span class="cursor"></span>

        </div>

    </div>

</div>


<!-- MONITOR STAND -->

<div class="stand"></div>

<div class="base"></div>


<!-- MUSIC PLAYER -->

<div class="player">


    <div class="song-title">

        🎧 Meri Mehbooba

    </div>


    <!-- VISUALIZER -->

    <div class="visualizer">

        <span class="bar"></span>

        <span class="bar"></span>

        <span class="bar"></span>

        <span class="bar"></span>

        <span class="bar"></span>

        <span class="bar"></span>

        <span class="bar"></span>

    </div>


    <!-- SONG -->

    <audio
        id="song"
        controls
        preload="metadata"
    >

        <source
            src="/static/song.mp3"
            type="audio/mpeg"
        >

        Your browser does not support audio.

    </audio>


</div>


</div>


<script>


const song =
    document.getElementById("song");


const lyricsScreen =
    document.getElementById("lyrics");


const container =
    document.querySelector(".container");


/*
====================================================
LYRICS
====================================================

IMPORTANT:

time = seconds

Neeche timing example hai.

Agar kisi line ko song ke 20 second par
dikhana hai:

{
    time: 20,
    text: "Your line"
}

Lyrics ke beech ke time ko apne song ke
actual timing ke according change kar sakte ho.

====================================================
*/


const lyrics = [


    {
        time: 0,
        text: "🎵 PLAY SONG 🎵"
    },


    {
        time: 5,
        text: "Kisi Roz Tumse Mulaakat Hogi"
    },


    {
        time: 10,
        text: "Meri Jaan Us Din Mere Saath Hogi"
    },


    {
        time: 15,
        text: "Magar Kab Na Jaane Yeh Barsaat Hogi"
    },


    {
        time: 20,
        text: "Mera Dil Hai Pyaasa Mera Dil Akela"
    },


    {
        time: 25,
        text: "Zara Tasveer Se Tu Nikal ke Saamne Aa"
    },


    {
        time: 30,
        text: "Meri Mehbooba 💜"
    },


    {
        time: 35,
        text: "Meri Taqdeer Hai Tu Machal ke Saamne Aa"
    },


    {
        time: 40,
        text: "Meri Mehbooba 💜"
    },


    {
        time: 45,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 50,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 55,
        text: "Zara Tasveer Se Tu Nikal ke Saamne Aa"
    },


    {
        time: 60,
        text: "Meri Mehbooba ❤️"
    },


    {
        time: 65,
        text: "Nahi Yaad Kabse Magar Main Hoon Jabse"
    },


    {
        time: 70,
        text: "Mere Dil Mein Teri Mohabbat Hai Tabse"
    },


    {
        time: 75,
        text: "Main Shaayar Hoon Tera Tu Meri Ghazal Hai"
    },


    {
        time: 80,
        text: "Badi Bekarari Mujhe Aaj Kal Hai"
    },


    {
        time: 85,
        text: "Badi Bekarari Mujhe Aaj Kal Hai"
    },


    {
        time: 90,
        text: "Mujhe Aaj Kal Hai"
    },


    {
        time: 95,
        text: "Tadap Kar Aayegi Woh"
    },


    {
        time: 100,
        text: "Tujhe Mil Jaayegi Woh"
    },


    {
        time: 105,
        text: "Meri Mehbooba 💜"
    },


    {
        time: 110,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 115,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 120,
        text: "Zara Tasveer Se Tu Nikal ke Saamne Aa"
    },


    {
        time: 125,
        text: "Meri Mehbooba ❤️"
    },


    {
        time: 130,
        text: "Meri Taqdeer Hai Tu Machal ke Saamne Aa"
    },


    {
        time: 135,
        text: "Meri Mehbooba 💜"
    },


    {
        time: 140,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 145,
        text: "Meri Mehbooba Meri Mehbooba"
    },


    {
        time: 150,
        text: "Meri Mehbooba 🎵"
    }

];



/* =========================
   PLAY
========================= */

song.addEventListener(
    "play",
    function() {

        container.classList.add(
            "playing"
        );

    }
);



/* =========================
   PAUSE
========================= */

song.addEventListener(
    "pause",
    function() {

        container.classList.remove(
            "playing"
        );

    }
);



/* =========================
   END
========================= */

song.addEventListener(
    "ended",
    function() {

        container.classList.remove(
            "playing"
        );

    }
);



/* =========================
   LYRICS CHANGE
========================= */

song.addEventListener(
    "timeupdate",
    function() {


        let currentLyric =
            lyrics[0];


        for (
            const line of lyrics
        ) {


            if (
                song.currentTime >=
                line.time
            ) {

                currentLyric =
                    line;

            }

        }


        if (

            lyricsScreen.dataset.line
            !== currentLyric.text

        ) {


            lyricsScreen.dataset.line =
                currentLyric.text;


            /*
               Restart animation
            */

            lyricsScreen.style.animation =
                "none";


            void lyricsScreen.offsetWidth;


            lyricsScreen.style.animation =
                "neonPulse 1.5s ease-in-out infinite alternate, lyricIn .5s ease";


            /*
               New lyric
            */

            lyricsScreen.innerHTML =

                currentLyric.text +

                '<span class="cursor"></span>';

        }

    }

);

</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
)
