# Imagepratice

Aplicativo web em Flask que recebe uma imagem e aplica um filtro do OpenCV. A imagem original e o resultado aparecem na mesma página.

## Filtros

- `blur`: desfoque gaussiano com kernel 15x15.
- `sharpen`: nitidez, com um kernel 3x3.
- `rotate`: rotação de 45 graus em torno do centro.

## Como rodar

```bash
pip install flask opencv-python numpy
python app.py
```

A página abre em http://127.0.0.1:5000. Envie uma imagem e escolha o filtro. A interface usa MaterializeCSS, carregado por CDN.

## Limitações

A imagem enviada é salva sempre como `static/uploads/original.png`, e o resultado como `static/uploads/processed.png`. O app trabalha com uma imagem por vez, e um novo envio sobrescreve a anterior.
