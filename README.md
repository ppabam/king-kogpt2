# king-kogpt2

- https://g.co/gemini/share/f4a9a21f945b
- [Pytorch 설치 - CUDA Toolkit, cuDNN 설치](https://stat-thon.tistory.com/104)
- [대통령 연설문](https://pypi.org/project/president-speech/)

### Gemini
- https://g.co/gemini/share/85788e6bcaea

### CUDA
```bash
# PyTorch가 CUDA를 인식하는지 , 현재 코드가 실행되는 환경의 PyTorch가 CUDA를 인식하고 있는지
$ pdm run python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
CUDA available: True


```