from pathlib import Path
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
AUDIO_WAV = ROOT / "assets" / "guia-esporte-adaptado.wav"
MEDIA = ROOT / "assets" / "media"
W, H = 1280, 720
GREEN = "#0B6E4F"
DARK = "#084F39"
INK = "#12211C"
ORANGE = "#FF6B35"
PAPER = "#F5F6F0"
WHITE = "#FFFFFF"
SENTENCES = [
    "O esporte adaptado abre caminhos para que mais pessoas participem do movimento, da convivência e da competição.",
    "Cada modalidade combina regras, equipamentos e apoios diferentes.",
    "Para começar, procure a secretaria de esporte da sua cidade ou consulte os clubes e Centros de Referência Paralímpica no site do Comitê Paralímpico Brasileiro.",
    "A prática deve respeitar a escolha da pessoa e contar com orientação profissional.",
    "O AdaptSport é um projeto acadêmico de informação.",
    "Ele não substitui avaliação médica, de fisioterapia ou orientação esportiva.",
]


def font(size: int, bold: bool = False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)


def wrap(draw, text, face, max_width):
    words, lines, current = text.split(), [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=face)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(draw, text, x, y, max_width, face, color, gap=16):
    lines = wrap(draw, text, face, max_width)
    for line in lines:
        draw.text((x, y), line, font=face, fill=color)
        y += face.size + gap
    return y


def wheelchair_athlete(draw, cx, cy, scale=1.0):
    s = scale
    r = int(116 * s)
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline=GREEN, width=max(8, int(12*s)))
    draw.ellipse((cx-10*s, cy-10*s, cx+10*s, cy+10*s), fill=GREEN)
    line = max(8, int(15*s))
    draw.line((cx, cy-48*s, cx, cy-136*s, cx+78*s, cy-170*s), fill=INK, width=line, joint="curve")
    draw.line((cx, cy-50*s, cx+118*s, cy-50*s), fill=INK, width=line)
    draw.line((cx, cy-46*s, cx-54*s, cy+55*s), fill=INK, width=line)
    draw.line((cx, cy+15*s, cx+68*s, cy+88*s), fill=INK, width=line)
    head = 35*s
    draw.ellipse((cx+55*s, cy-214*s, cx+55*s+2*head, cy-214*s+2*head), fill=INK)
    draw.ellipse((cx+r+38*s, cy+r-15*s, cx+r+72*s, cy+r+19*s), outline=GREEN, width=max(6, int(9*s)))
    draw.line((cx-260*s, cy+150*s, cx-145*s, cy+150*s), fill=ORANGE, width=max(8, int(12*s)))
    draw.line((cx-238*s, cy+185*s, cx-150*s, cy+185*s), fill=ORANGE, width=max(5, int(8*s)))


def create_scenes(directory: Path):
    scenes = []
    # Capa: preserva as cores do MVP e usa uma ilustração vetorial autoral.
    image = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((52, 52, 1228, 668), radius=36, fill=WHITE, outline="#DCE1D6", width=3)
    d.rounded_rectangle((82, 83, 490, 130), radius=20, fill="#E3F0E9")
    d.text((104, 92), "ADAPTSPORT · GUIA ACESSÍVEL", font=font(22, True), fill=DARK)
    text_block(d, "Esporte adaptado", 92, 185, 590, font(56, True), INK, 8)
    text_block(d, "Movimento, convivência e escolha.", 94, 342, 540, font(32), GREEN, 10)
    wheelchair_athlete(d, 930, 465, .8)
    d.rounded_rectangle((90, 572, 642, 630), radius=28, fill=ORANGE)
    d.text((118, 585), "Informação para participar", font=font(25, True), fill=INK)
    first = directory / "scene-1.png"
    image.save(first)
    scenes.append(first)

    # Scene two: adaptações e apoios escritos em linguagem simples.
    image = Image.new("RGB", (W, H), DARK)
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((56, 48, 1224, 670), radius=38, fill=GREEN)
    d.text((94, 88), "CADA MODALIDADE TEM UM JEITO", font=font(24, True), fill="#D7F0E2")
    text_block(d, "Regras, equipamentos e apoios diferentes.", 94, 160, 1000, font(50, True), WHITE, 12)
    labels = [("01", "Modalidades"), ("02", "Acessos"), ("03", "Apoios")]
    for index, (number, label) in enumerate(labels):
        x = 100 + index * 365
        d.rounded_rectangle((x, 415, x+320, 565), radius=24, fill=WHITE)
        d.ellipse((x+22, 451, x+84, 513), fill=ORANGE)
        d.text((x+35, 463), number, font=font(22, True), fill=INK)
        d.text((x+102, 462), label, font=font(27, True), fill=INK)
    second = directory / "scene-2.png"
    image.save(second)
    scenes.append(second)

    # Scene three: ação sem prometer vagas ou serviços que o projeto não oferece.
    image = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(image)
    d.rectangle((0, 0, W, 24), fill=ORANGE)
    d.text((95, 105), "QUER COMEÇAR?", font=font(26, True), fill=GREEN)
    text_block(d, "Procure. Pergunte. Experimente.", 92, 175, 1050, font(52, True), INK, 12)
    text_block(d, "Consulte serviços municipais e diretórios oficiais do Comitê Paralímpico Brasileiro.", 95, 335, 1030, font(31), INK, 14)
    d.rounded_rectangle((94, 525, 800, 605), radius=32, fill=GREEN)
    d.text((128, 544), "Respeite a escolha e o ritmo de cada pessoa.", font=font(27, True), fill=WHITE)
    third = directory / "scene-3.png"
    image.save(third)
    scenes.append(third)
    return scenes


def vtt_time(seconds: float) -> str:
    ms = round(seconds * 1000)
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, milli = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{milli:03d}"


def main():
    if not AUDIO_WAV.exists():
        raise SystemExit(f"Áudio-base ausente: {AUDIO_WAV}")
    MEDIA.mkdir(parents=True, exist_ok=True)
    mp3 = MEDIA / "guia-esporte-adaptado.mp3"
    video = MEDIA / "guia-esporte-adaptado.mp4"
    poster = MEDIA / "video-poster.png"
    captions = MEDIA / "guia-esporte-adaptado.vtt"

    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(AUDIO_WAV), "-codec:a", "libmp3lame", "-b:a", "96k", str(mp3)], check=True)
    info = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(AUDIO_WAV)], text=True)
    duration = float(info.strip())

    with tempfile.TemporaryDirectory(prefix="adaptsport-media-") as tmp:
        temp = Path(tmp)
        scenes = create_scenes(temp)
        Image.open(scenes[0]).save(poster)
        segment = duration / len(scenes)
        command = ["ffmpeg", "-y", "-loglevel", "error"]
        for scene in scenes:
            command.extend(["-loop", "1", "-framerate", "30", "-t", f"{segment:.3f}", "-i", str(scene)])
        command.extend(["-i", str(AUDIO_WAV)])
        graph = []
        for index in range(len(scenes)):
            graph.append(f"[{index}:v]scale={W}:{H},fps=30,format=yuv420p,trim=duration={segment:.3f},setpts=PTS-STARTPTS[v{index}]")
        graph.append("".join(f"[v{index}]" for index in range(len(scenes))) + f"concat=n={len(scenes)}:v=1:a=0[vout]")
        command.extend(["-filter_complex", ";".join(graph), "-map", "[vout]", "-map", f"{len(scenes)}:a:0", "-t", f"{duration:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "25", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(video)])
        subprocess.run(command, check=True)

    # Distribui as legendas proporcionalmente à quantidade de palavras de cada frase.
    weights = [len(sentence.split()) for sentence in SENTENCES]
    total_words = sum(weights)
    current = 0.0
    lines = ["WEBVTT", ""]
    for index, (sentence, weight) in enumerate(zip(SENTENCES, weights), start=1):
        start = current
        current = duration if index == len(SENTENCES) else current + duration * weight / total_words
        lines.extend([str(index), f"{vtt_time(start)} --> {vtt_time(current)}", sentence, ""])
    captions.write_text("\n".join(lines), encoding="utf-8")
    print(f"MP3: {mp3} ({mp3.stat().st_size} bytes)")
    print(f"MP4: {video} ({video.stat().st_size} bytes, {duration:.2f}s)")
    print(f"Poster: {poster}")
    print(f"Legendas: {captions}")


if __name__ == "__main__":
    main()
