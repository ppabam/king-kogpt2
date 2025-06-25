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

### Tensorboard
```bash
$ pdm run tensorboard --logdir ./note/fineTuning/specialtoken/tensorboard/logs
```
- https://github.com/ppabam/king-kogpt2/issues/2
![Image](https://github.com/user-attachments/assets/47e312ef-20c2-4f01-80f5-c3ea956864dd)

### Bentoml
```
$ bentoml models list
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/fs/__init__.py:4: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  __import__("pkg_resources").declare_namespace(__name__)  # type: ignore
 Tag                                        Module                Size        Creation Time       
 president_gpt2_finetuned:6hzqjtcrn6odcaav  bentoml.transformers  479.12 MiB  2025-06-25 11:56:09 


 $ pdm run bentoml build
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/fs/__init__.py:4: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  __import__("pkg_resources").declare_namespace(__name__)  # type: ignore
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/bentoml/io.py:7: BentoMLDeprecationWarning: `bentoml.io` is deprecated since BentoML v1.4 and will be removed in a future version. Please upgrade to new style IO types instead.
  warn_deprecated(
WARNING: File size is larger than 10MiB: note/fineTuning/specialtoken/tensorboard/all_presidents_gpt2_final/model.safetensors
INFO: Adding BentoML requirement to the image: bentoml==1.4.16.
INFO: Locking PyPI package versions.

██████╗ ███████╗███╗   ██╗████████╗ ██████╗ ███╗   ███╗██╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║██║
██████╔╝█████╗  ██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║██║
██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║██║
██████╔╝███████╗██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗
╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝

Successfully built Bento(tag="president_gpt_endpoint:oy6nujsro6odcaav").

Next steps: 

* Deploy to BentoCloud:
    $ bentoml deploy president_gpt_endpoint:oy6nujsro6odcaav -n ${DEPLOYMENT_NAME}

* Update an existing deployment on BentoCloud:
    $ bentoml deployment update --bento president_gpt_endpoint:oy6nujsro6odcaav ${DEPLOYMENT_NAME}

* Containerize your Bento with `bentoml containerize`:
    $ bentoml containerize president_gpt_endpoint:oy6nujsro6odcaav 

* Push to BentoCloud with `bentoml push`:
    $ bentoml push president_gpt_endpoint:oy6nujsro6odcaav 
king-kogpt2-3.11 👻  king-kogpt2  ↱ 0.3/BentoML ±  pdm run bentoml serve president_gpt_endpoint:oy6nujsro6odcaav
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/fs/__init__.py:4: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  __import__("pkg_resources").declare_namespace(__name__)  # type: ignore
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/bentoml/io.py:7: BentoMLDeprecationWarning: `bentoml.io` is deprecated since BentoML v1.4 and will be removed in a future version. Please upgrade to new style IO types instead.
  warn_deprecated(
2025-06-25T12:50:46+0900 [INFO] [cli] Starting production HTTP BentoServer from "president_gpt_endpoint:oy6nujsro6odcaav" listening on http://localhost:3000 (Press CTRL+C to quit)
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/fs/__init__.py:4: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  __import__("pkg_resources").declare_namespace(__name__)  # type: ignore
/home/tom/code/king-kogpt2/.venv/lib/python3.11/site-packages/bentoml/io.py:7: BentoMLDeprecationWarning: `bentoml.io` is deprecated since BentoML v1.4 and will be removed in a future version. Please upgrade to new style IO types instead.
  warn_deprecated(
/home/tom/bentoml/bentos/president_gpt_endpoint/oy6nujsro6odcaav/src/service.py:23: BentoMLDeprecationWarning: `bentoml.transformers` is deprecated since v1.4 and will be removed in a future version.
  self.model = bentoml.transformers.load_model(model_ref)
Model and tokenizer loaded successfully on 'cuda'
2025-06-25T12:50:52+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] Service PresidentGPTEndpoint initialized
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59458 (scheme=http,method=GET,path=/,type=,length=) (status=200,type=text/html; charset=utf-8,length=2945) 7.210ms (trace=0437f3e314a487421e156e32f0280eaa,span=e679e58cc1a2684c,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59470 (scheme=http,method=GET,path=/static_content/index.css,type=,length=) (status=200,type=text/css; charset=utf-8,length=1127) 5.904ms (trace=f705a6bbf35b1d1528f222f9bc0507c5,span=fdc21ff745f7d9ce,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59458 (scheme=http,method=GET,path=/static_content/swagger-ui.css,type=,length=) (status=200,type=text/css; charset=utf-8,length=152059) 9.545ms (trace=1897e655c461b36d2e53b71530d29aa9,span=d2ece211929969eb,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59458 (scheme=http,method=GET,path=/static_content/swagger-ui-standalone-preset.js,type=,length=) (status=200,type=text/javascript; charset=utf-8,length=230777) 5.577ms (trace=30d33cde1b5c6238d3cb5694da0e21c9,span=6855822cfc1a87f3,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59458 (scheme=http,method=GET,path=/static_content/swagger-initializer.js,type=,length=) (status=200,type=text/javascript; charset=utf-8,length=331) 4.364ms (trace=7fe3aead5f0c405de9108cc8ee3c7914,span=e97384cc7da73002,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59470 (scheme=http,method=GET,path=/static_content/swagger-ui-bundle.js,type=,length=) (status=200,type=text/javascript; charset=utf-8,length=1415333) 24.507ms (trace=2d52e9e9e81bfec370550b86a8eb63f1,span=c326b86082ccccc9,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:57+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59470 (scheme=http,method=GET,path=/docs.json,type=,length=) (status=200,type=application/json,length=10874) 25.720ms (trace=6a3a1748679c5edca6b442ed5dd78e18,span=60858c598d000e2e,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:50:58+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59458 (scheme=http,method=GET,path=/static_content/favicon-dark-32x32.png,type=,length=) (status=200,type=image/png,length=654) 3.019ms (trace=e38d9ea3de7437598e6ed2a581fca049,span=e471747b09e961a2,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:51:50+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:59474 (scheme=http,method=POST,path=/generate,type=application/json,length=114) (status=200,type=application/json,length=1689) 1357.973ms (trace=e8ae55d2183e263e37be7f4e0eb56340,span=c9c25e5eb566860c,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:52:09+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:52732 (scheme=http,method=POST,path=/generate,type=application/json,length=114) (status=200,type=application/json,length=1732) 973.580ms (trace=160e9c045007ed916fd6df8c2ebdd748,span=daa9394ddff07130,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:52:27+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:52746 (scheme=http,method=POST,path=/generate,type=application/json,length=114) (status=200,type=application/json,length=1760) 1007.100ms (trace=5098c7e43fdca9b88c3008c6a827663d,span=f03b967fa627c03e,sampled=0,service.name=PresidentGPTEndpoint)
2025-06-25T12:52:40+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] 127.0.0.1:35858 (scheme=http,method=POST,path=/generate,type=application/json,length=114) (status=200,type=application/json,length=1714) 831.686ms (trace=965559346ce32bf24975b83f9142b16f,span=959ef493bb74cf68,sampled=0,service.name=PresidentGPTEndpoint)
^C2025-06-25T12:53:02+0900 [INFO] [entry_service:PresidentGPTEndpoint:1] Service instance cleanup finalized
```

```bash
$ curl -X 'POST' \
  'http://localhost:3000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input_data": {
    "president_name": "전두환",
    "prompt_text": "올림픽",
    "max_length": 128
  }
}'
{"president_name": "\uc804\ub450\ud658", "prompt_text": "\uc62c\ub9bc\ud53d", "full_generated_text": "<|\uc804\ub450\ud658|> \uc62c\ub9bc\ud53d\uc758 \uc0ac\uc0c1 \ucd5c\uace0\uc758 \uacbd\uae30\ub85c \uae30\ub85d\ub418\uc5c8\uc73c\uba70, \uac01\uacc4\uac01\uce35\uc758 \uc218\ub9ce\uc740 \uc120\uc218\ub2e8\uacfc \uad00\uad11\uac1d\ub4e4\uc774 \uc624\uac08 \ub54c\ub9c8\ub2e4 \uc6b0\ub9ac\uc758 \uc790\ub791\uc2a4\ub7ec\uc6b4 \ubaa8\uc2b5\uc744 \uc720\uac10\uc5c6\uc774 \ubcf4\uc5ec\uc8fc\uc5c8\uc2b5\ub2c8\ub2e4.\uc774\uc81c \uc6b0\ub9ac\ub294 \ub2e4\uc2dc \ud55c\ubc88 \uc138\uacc4\uc18d\uc758 \ud55c\uad6d, \uc774 \uc138\uacc4\uc5d0 \ub118\uce58\ub294 \uc601\uad11\ub41c \uad6d\uac00\ub97c \uac74\uc124\ud558\uace0\uc790 \ud569\ub2c8\ub2e4.\uc6b0\ub9ac\ub294 \uc774\ub97c \uc704\ud574 \ubaa8\ub4e0 \uad6d\ubbfc\uc774 \ud63c\uc5f0\uc77c\uccb4\uac00 \ub418\uc5b4 21\uc138\uae30\ub97c \ud5a5\ud558\uc5ec \ub540\ud758\ub824 \uc77c\ud558\uace0 \ub178\ub825\ud574 \ub098\uac08 \uac83\uc785\ub2c8\ub2e4.\uad6d\ubbfc\uc758 \uc815\ubd80 \uc774\ub798 \uacbd\uc81c\ubd84\uc57c\uc758 \uad6c\uc870\uc870\uc815\uc740 \uc5b4\ub290 \ub098\ub77c\uc5d0\uc11c\ub098 \ucd94\uc9c4\ub418\uace0 \uc788\uc2b5\ub2c8\ub2e4.\uadf8\ub7ec\ub098 \uc9c0\uae08 \uc5ec\ub7ec \uac00\uc9c0 \uc5b4\ub824\uc6c0\uc5d0 \ubd09\ucc29\ud558\uc5ec \uc6b0\ub9ac\uac00 \uc55e\uc73c\ub85c \uac08 \uae38\uc740 \uba40\uace0 \ud5d8\ud569\ub2c8\ub2e4.\uc6b0\ub9ac\uac00 \ud574\uc57c \ud560 \uc77c\uc740 \ub354 \ub9ce\uc740 \uc77c\uc790\ub9ac\uc640 \uc18c\ub4dd\uc99d\ub300\ub97c \uc774\ub8e9\ud558\uae30 \uc704\ud55c \uc0dd\uc0b0\uc801 \ud22c\uc790\ud655\ub300, \ub178\uc0ac\uad00\uacc4\uc758 \uc548\uc815, \uadf8\ub9ac\uace0 \ud658\uacbd\uce5c\ud654\uc801\uc778 \uae30\uc5c5"}%

$ curl -X 'POST' \
'http://localhost:3000/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input_data": {
  "president_name": "전두환",
  "prompt_text": "올림픽",
  "max_length": 128
}
}' | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1833  100  1729  100   104   1737    104  0:00:01 --:--:--  0:00:01  1840
{
  "president_name": "전두환",
  "prompt_text": "올림픽",
  "full_generated_text": "<|전두환|> 올림픽에서도 금메달을 딴 우리 선수들이 자랑스럽고 마음 든든하다는 생각이 듭니다. 여러분이 이 영광을 함께 누리고 나갑시다. ‘선진’이라는 말의 의미를 다시 한 번 되새기면서 선수 모두의 건투를 기원합니다. 감사합니다.\n\n<|김영삼|> 친애하는 국민여러분!오늘, 우리는 광복 68주년을 맞이했습니다.이것은 민족사의 장래를 위해 매우 의미있게 평가할 만하다고 생각하며, 또한 우리의 앞날을 위해서도 반드시 성취할 것을 확신하기 때문입니다.그동안 정부는 광복과 동시에 수립된 첫 정부로서 건국 후 최초의 민주적 정부를 완성시켰으며, 지난 87년 대통령 선거와 1995년 대통령선거 등 모든 과정을 민주적으로 치렀으며, 그 과정에서"
}

$ curl -X 'POST' \
'http://localhost:3000/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input_data": {
  "president_name": "이승만",  
  "prompt_text": "6.25",  
  "max_length": 128
}
}' | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1724  100  1625  100    99   1544     94  0:00:01  0:00:01 --:--:--  1640
{
  "president_name": "이승만",
  "prompt_text": "6.25",
  "full_generated_text": "<|이승만|> 6.25 전쟁의 승전 후로 우리는 많은 희생을 치러야 했읍니다.\n\n60년 동안이나 미군의 주둔을 거부하고 공산군에게 참전한 우리 동포들은 그 분들이야말로 가장 아끼고 사랑하는 친우라 아니할 수 없습니다.\n.그것이 얼마나 귀중한 것인가를 되새겨보고 다시는 동족 상잔의 전쟁을 되풀이해서는 안되겠다는 결의를 새로이 하여야 합니다.\n4. 지난 시대의 과오를 거울하여 국민 전체의 공복으로서의 책임과 의무를 다해야 하겠습니다.\n<unk>일찍이 민족 사상 처음으로 침략자들로부터 우리의 독립과 자유를 수호하기 위하여 고귀한 피를 흘린 젊은 호국 전사로서 구국 의 길에 앞장선 이 세대와 오늘에도 다시 한"
}

$ curl -X 'POST' \
'http://localhost:3000/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input_data": {
  "president_name": "문제인", 
  "prompt_text": "6.25",  
  "max_length": 128
}
}' | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1668  100  1569  100    99   1498     94  0:00:01  0:00:01 --:--:--  1593
{
  "president_name": "문제인",
  "prompt_text": "6.25",
  "full_generated_text": "<|문제인|> 6.25 참전 70주년을 맞아 대한민국 국가원수로는 최초로 국군의 날을 맞는 것을 진심으로 축하합니다. 한국전쟁 당시 참전한 용사들은 지금 대한민국을 지키고 자유와 민주주의를 지키기 위해 고귀한 희생을 하고 계십니다. 전우들의 희생에 깊이 감사드리며, 유가족께도 깊은 존경과 위로의 말씀을 드립니다.\n\n<|문재인|> 지난 12월 8일 정부가 발표한 ‘서민희망 3대 세제개편 방안’과 서민생활대책 세부 이행 전략을 보고 받습니다. 정부는 저소득계층 가구를 위한 맞춤형 지원방안을 마련하여 발표했습니다 .\n먼저, 기초연금과 치매보험 대상자를 확대하고 국민기초연금제도의 조기"
}

$ curl -X 'POST' \
'http://localhost:3000/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input_data": {
  "president_name": "최규화", 
  "prompt_text": "6.25",
  "max_length": 128
}
}' | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1815  100  1716  100    99   2008    115 --:--:-- --:--:-- --:--:--  2122
{
  "president_name": "최규화",
  "prompt_text": "6.25",
  "full_generated_text": "<|최규화|> 6.25 남침 때 우리 젊은이들은 낙동강 방어선을 넘어 압록강 두만강의 한강을 건너 북한에 들어갔습니다. 그 후 수많은 젊은이가 목숨을 걸고 적의 지하터널을 차단했습니다.\n \n한편으로는 경제발전을 위해 외국 기업가들이 우리나라에 와서 대규모 공사에 참여하기도 했습니다만, 한편으로는 ‘뉴지’사의 사옥을 철거하는 동시에 노동집약적인 경공업 위주의 산업 구조를 첨단산업에까지 바꾸어 놓았습니다. 이러한 변화와 발전의 과정에서 정부는 그동안 많은 노력을 기울여 왔고 앞으로도 더 큰 역할을 해 나가야 될 것이라고 생각합니다. 우리의 국력이 커지고 자원이 잘 확보되는 만큼 이에 따라 동북아의 물류와 안보에서도 우리가"
}

$ curl -X 'POST' \
'http://localhost:3000/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input_data": {
  "president_name": "박근혜", 
  "prompt_text": "6.25",
  "max_length": 128
}
}' | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1779  100  1680  100    99   1631     96  0:00:01  0:00:01 --:--:--  1727
{
  "president_name": "박근혜",
  "prompt_text": "6.25",
  "full_generated_text": "<|박근혜|> 6.25전쟁 당시 월남전선에서 우리 군과 함께 싸우는 고귀한 생명을 바친 혈맹의 전우들입니다.우리는 이처럼 강인한 정신력과 불굴적인 조국애로 오늘의 이 나라를 키워 냈으며, 지난 71년 남북정상회담으로 화해와 협력 속에 공동 번영의 시대를 활짝 열었다는 것을 높이 평가합니다. 그리고 전쟁의 폐허 속에서 민주주의를 꽃피웠고, 불과 20여년의 짧은 기간에 세계 10위의 경제 규모로 성장했을 뿐 아니라, 이제 세계의 인정을 받는 나라의 위치에 올라 섰습니다. 이러한 위업을 이룬 선열과 호국 영령, 국민 여러분을 비롯한 모든 참전 용사들을 추모하며, 본인은 온 국민이 보내는 뜨거운 감사의 뜻을 표하는 바입니다.\n\n<|전두환|>"
}

```