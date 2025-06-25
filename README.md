# king-kogpt2

### Docs
- [Gemini](https://g.co/gemini/share/f4a9a21f945b)
- [Pytorch 설치 - CUDA Toolkit, cuDNN 설치](https://stat-thon.tistory.com/104)
- [대통령 연설문](https://pypi.org/project/president-speech/)
- [PyTorch 딥러닝 챗봇](https://wikidocs.net/book/7439)

### Gemini
- https://g.co/gemini/share/85788e6bcaea

### CUDA
```bash
# PyTorch가 CUDA를 인식하는지 , 현재 코드가 실행되는 환경의 PyTorch가 CUDA를 인식하고 있는지
$ pdm run python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
CUDA available: True
```

```bash
$ nvidia-smi
Wed Jun 25 09:39:21 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.72                 Driver Version: 566.14         CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0  On |                  N/A |
| N/A   74C    P0             75W /   85W |    5334MiB /   8188MiB |     96%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A    365723      C   /python3.11                                 N/A      |
+-----------------------------------------------------------------------------------------+
```

```
nvidia-smi 결과 분석: 하드웨어의 상태를 알려줍니다.
먼저, 현재 nvidia-smi 결과가 왜 좋은 신호인지 알려드리겠습니다.

- Temp: 74C: GPU 온도가 74도로, 열심히 일하고 있다는 의미입니다. (일반적으로 70~85도는 정상 범위입니다.)
P- erf: P0: P0는 GPU가 최대 성능(Maximum Performance) 상태로 작동하고 있음을 나타냅니다.
- Pwr:Usage/Cap: 75W / 85W: 최대 전력의 상당 부분(약 88%)을 사용하며 활발히 연산 중입니다.
- Memory-Usage: 5334MiB / 8188MiB: 전체 8GB VRAM 중 약 5.3GB를 모델과 데이터가 차지하고 있습니다. GPU 메모리를 잘 활용하고 있다는 뜻입니다.
- GPU-Util: 96%: 가장 중요한 지표입니다. GPU의 연산 코어가 거의 100%에 가깝게 사용되고 있다는 의미로, GPU가 쉬지 않고 계속해서 계산 작업을 처리하고 있다는 뜻입니다.
- Processes: /python3.11: 현재 GPU를 사용하는 프로세스가 바로 우리의 파이썬 학습 스크립트임을 확인시켜 줍니다.

결론: nvidia-smi는 "내 GPU가 지금 놀지 않고 열심히 일하고 있는가?" 라는 질문에 "네, 거의 모든 힘을 다해 일하고 있습니다!" 라고 답해주고 있습니다.
```