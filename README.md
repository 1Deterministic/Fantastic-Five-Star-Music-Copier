# Fantastic Five Star Music Copier
**[Português](#português)**  
**[English](#english)**  

## Português

`ffsmc` é uma ferramenta em linha de comando para encontrar e copiar músicas `.mp3` avaliadas com 5 estrelas em uma pasta e suas subpastas para uma outra pasta, útil para sincronizar apenas o melhor da sua biblioteca com seu smartphone, por exemplo, com menor capacidade de armazenamento. Uma vez que você já realizou a cópia uma vez e deseja atualizar, ele pode copiar apenas as músicas que estão faltando no destino, para agilizar o processo. E ainda, caso haja músicas cuja avaliação diminuiu na pasta de origem ou que foram apagadas de lá, você pode ordenar que elas sejam apagadas no destino também. Suporta apenas `.mp3` até o momento.


## Meu caso de uso

Desenvolvi o `ffsmc` como uma forma de ajudar a organizar minha própria biblioteca mas acredito que possa ser útil para mais alguém em situação parecida, o que me motivou a publicar o código. Eu tenho uma pasta de arquivos que contém minha pasta de músicas e costumo guardar discografias inteiras ainda que não ouça tudo, já que sempre estou revendo minhas preferências. Também possuo uma outra pasta de arquivos que é sincronizada com meu smartphone, usando o **[syncthing](https://syncthing.net/)**. O `ffsmc` entra na interface entre essas duas pastas: eu copio as faixas que avaliei como melhores para a pasta sincronizada com o smartphone, para que o `syncthing` as envie quando for oportuno. Não sobrescrevo os arquivos no destino, para que a cópia seja mais rápida e para que qualquer conversão para um bitrate menor (para preservar espaço) que eu fizer permaneça. Em compensação, quero que as músicas que não avalio mais como 5 estrelas sejam apagadas do destino, o que o `ffsmc` também faz por mim.


## Utilização

* `ffsmc.exe -source "pasta_de_origem" -destination "pasta_destino" [-override_on_destination] [-delete_left_files]`  
* Opções entre colchetes são opcionais  
* O parâmetro após `-source` deve ser a pasta de origem  
* O parâmetro após `-destination` deve ser a pasta destino  
* `-override_on_destination` realiza a cópia de todos os arquivos, sobrescrevendo os que já estiverem na pasta destino. Caso não seja recebido, será feita a cópia apenas dos arquivos que estiverem faltando  
* `-delete_left_files apaga` todos os arquivos da pasta destino que não forem encontrados na busca, ou que não tenham satisfeito às condições para seleção (possuir 5 estrelas de avaliação). Caso não seja recebido, eles serão ignorados  
* Você deve utilizar a extensão `.exe` mesmo rodando em Linux. É uma peculiaridade da exportação standalone feita com o nuitka que mantive  
* Note que, por enquanto, a única verificação de igualdade feita em `-override_on_destination` e `-delete_left_files`  é baseada no nome do arquivo  



## English

`ffsmc` is a command line tool to find and copy `.mp3` music rated as 5 stars from a folder and its subfolders and paste them to another folder, useful to synchronize only the best of your music library with your smartphone, for instance, with less storage capability. Once you already executed once and you want to update it, it can also copy/paste only the files that are not yet on destination to speedup the process. Also, if there are any music that was down-rated or deleted on the source folder, you can order it to delete them on destination too. Supports only `.mp3` at the moment.


## My use case

I developed `ffsmc` as a way to help me organize my own library but I believe it can be useful for someone in a similar situation, wich motivated me to publish the code. I have a folder of files that contains my music folder and I usually store whole discographies even if I dont listen to all of it, because I'm always reconsidering my preferences. I also have another folder that is synchronized with my smartphone, using the awesome **[syncthing](https://syncthing.net/)**. `ffsmc` comes at the interface between these two  folders: I copy/paste the tracks I rated as the best to my folder synchronized with my smartphone, for `syncthing` to sync them when it's convenient. I don't override the files on the destination folder, to execute faster and to maintain any conversion to a lower bitrate (to save storage space) I eventually do. However, I want the music I don't rate as 5 stars anymore to be deleted from the destination, what `ffsmc` also does for me.


## Utilization

* `ffsmc.exe -source "source_folder" -destination "destination_folder" [-override_on_destination] [-delete_left_files]`  
* Options between brackets are optional
* The argument after `-source` must be the source folder  
* The argument after `-destination` must be the destination folder  
* `-override_on_destination` copy/paste all files, overwriting those already on destination. If it's not received, it will copy/paste only the files needed  
* `-delete_left_files` deletes all the files on destination that wasn't found during the scan, or don't match the requisites to be selected (have a rating of 5 stars). If it's not received, they will be ignored  
* You must use `.exe` extension even running on Linux. It is a peculiarity of standalone export using nuitka I kept  
* Notice that, for now, the only equality check made in `-override_on_destination` and `-delete_left_files` is based on the file name  


## [1Deterministic](https://github.com/1Deterministic), 2018
