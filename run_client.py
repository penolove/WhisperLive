from whisper_live.client import TranscriptionClient

def main():
    # 初始化客户端
    client = TranscriptionClient(
        host="localhost",  # 服务器地址
        port=9090,        # 服务器端口
        model="medium",
        use_vad=True,     # 启用语音活动检测
        lang="zh",        # 设置为中文
        log_transcription=False,
        # compute_type="int8",
        # 可选：设置输出文件路径
        output_transcription_path="./transcription.srt",
        # 可选：保存录音
        save_output_recording=True,
    )

    # 开始转录
    # 这将开始录音并实时转录
    # client('example.wav')
    client('test-yt.mp3')

if __name__ == "__main__":
    main()