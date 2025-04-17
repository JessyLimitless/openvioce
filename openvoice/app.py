# ✅ 1. Checkpoints 업로드
from google.colab import files
import zipfile, os

uploaded = files.upload()  # zip 파일 업로드

# 압축 해제
for fname in uploaded.keys():
    if fname.endswith(".zip"):
        with zipfile.ZipFile(fname, 'r') as zip_ref:
            zip_ref.extractall("checkpoints")

# ✅ 2. 저장소 클론 및 설치
!git clone https://github.com/myshell-ai/OpenVoice.git
%cd OpenVoice
!pip install -r requirements.txt
!pip install git+https://github.com/myshell-ai/MeloTTS.git
!python -m unidic download

# ✅ 3. sys.path 설정 (모듈 인식용)
import sys
sys.path.append('/content/OpenVoice')

# ✅ 4. 예시 텍스트 → 음성
from openvoice.api import TTS
import IPython.display as ipd

model = TTS(language='KO')
text = "안녕하세요, 뮤즈 에이아이입니다. 만나서 반가워요."
output_path = "output.wav"
model.tts_to_file(text, speaker='default', file_path=output_path)

# ✅ 5. 오디오 자동 재생
ipd.Audio(output_path)
