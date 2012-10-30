pyserial-conection
==================

Binarización de una imagen y envio a través de Conexión serial utilizando [PIL](http://www.pythonware.com/products/pil/) y [pyserial](http://pyserial.sourceforge.net), `python`

__Uso__<br />
```python
python scon.py ImgIn [ImgOut]
```

*ImgIn: Ruta de la imagen a binarizar y enviar*<br />
*ImgOut: Nombre de la imagen binarizada para ser guardada.*


__Notas Técnicas__<br />
* FPGA: Nexys 2
* Implementación de RAM por bloques.
* Ram con 20 bloques, cada uno de 16Kbits. En total 320Kbits
* Tamaño por pixel: 8 bits
* Tamaño Máximo de imágen a enviar: `320k/8 = 40k` -> 200x200 px

__Universidad Tecnológica de Pereira - Ingieneria en Sistemas y Computación__


__Autores__
* Jonathan Alvarez Gonzalez [@jonalvarezz](https://twitter.com/jonalvarezz)
* Juan David Corrales 

__GitHub__ <br />
https://github.com/jonalvarezg/pyserial-conection/

__License__<br />
Free Share

