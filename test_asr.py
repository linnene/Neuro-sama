from faster_whisper import WhisperModel
import os

class WhisperTranscriber:
    def __init__(self, model_size="tiny", device="cpu", compute_type="int8"):
        print(f"正在加载模型: {model_size} ({device})...")
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        print(f"模型加载完成: {model_size} ({device})...")


    def run(self, audio_path, output_dir="outputs"):
        if not os.path.exists(audio_path):
            print(f"错误: 找不到文件 {audio_path}")
            return

        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.txt")

        print(f"正在转录: {audio_path}...")
        segments, info = self.model.transcribe(
                    audio_path, 
                    beam_size=5,
                    language="zh",          # 强制中文，减少误判
                    vad_filter=True,        # 过滤静音/噪音
                    vad_parameters=dict(min_silence_duration_ms=500), # 超过0.5秒静音自动切分
                    initial_prompt="以下是普通话内容，请准确转录。" # 引导词，可以减少语气词
                )
        print(f"语言检测: {info.language} (置信度: {info.language_probability:.2f})")

        with open(output_path, "w", encoding="utf-8") as f:
            for segment in segments:
                line = f"[{segment.start:>6.2f}s -> {segment.end:>6.2f}s] {segment.text}"
                print(line)
                f.write(line + "\n")
        
        print(f"--- 转录完成，结果已保存至: {output_path} ---")

if __name__ == "__main__":
    # 初始化
    # 如果后续 CUDA 可用了，把这里改为 device="cuda", compute_type="float16"
    app = WhisperTranscriber(model_size="tiny", device="cpu", compute_type="int8")
    
    # 填入你实际的音频路径
    test_audio = "data/raw/audio/example.wav" 
    if os.path.exists(test_audio):
        app.run(test_audio)
    else:
        print(f"请将音频文件命名为 {test_audio} 放在当前目录下，或者修改代码中的路径。")