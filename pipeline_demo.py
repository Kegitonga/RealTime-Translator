"""pipeline_demo.py - connects ASR, translator, and TTS (stubs)
Replace stubs with cloud providers (Google, Azure, AWS) for production.
"""
def asr_stub(audio):
    return 'Hello from Nairobi'

def translate_stub(text, target='sw'):
    return 'Habari kutoka Nairobi' if target=='sw' else text

def tts_stub(text):
    return f'[AUDIO for: {text}]'

if __name__ == '__main__':
    txt = asr_stub(None)
    tr = translate_stub(txt, 'sw')
    audio = tts_stub(tr)
    print(txt)
    print(tr)
    print(audio)
