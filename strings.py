# localization strings

name = "Fantastic Five Star Music Copier"
version = "0.2-alpha"
codename = "Breaking the Law"

en = {
    "version": name + " " + version + ": " + codename,
    "invalid path": "Some of the paths received is not a folder.",
    "missing required arguments": "Missing -source or -destination arguments. Try ffsmc.exe -h to see the help.",
    "missing folder path": "Missing folder path after -source or -destination arguments. Try ffsmc.exe -h to see the help.",
    "invalid size": "Negative, not integer or not numerical size received.",
    "missing size limit": "Missing size limit after -size_limit. Try ffsmc.exe -h to see the help.",
    "scanning source": "Scanning source folder...",
    "copying new files": "Copying new files...",
    "error": "Error: ",
    "not copied": " was not copied.",
    "not deleted": " was not deleted.",
    "safe exit": "Exiting for safety.",
    "size limit reached": "Size limit reached.",
    "copied file not found": "Error: copied file not found inside destination folder.",
    "deleting left files": "Deleting left files...",
    "done": "Done!",
    "help": name + " " + version + ": " + codename + "\n" +
"""ffsmc.exe -source "source_folder" -destination "destination_folder" [options]
Options are:
    -h, shows this help screen.
    -source "source_folder", sets the source folder to search for music. "source_folder" is the path of the source folder and must be right after -source. The use of quotes is recommended.
    -destination "destination folder", sets the destination folder to copy music to. "destination_folder" is the path of the destination folder and must be right after -destination. The use of quotes is recommended.
    -override_on_destination, copy/paste all files, overwriting those already on destination. If it's not received, it will copy/paste only the files needed.  
    -delete_left_files, deletes all the files on destination that wasn't found on the source during the scan, don't match the requisites to be selected (have 5 stars of rating) or was not copied due to use of -size_limit. If it's not received, they will be ignored.
    -size_limit size_in_megabytes, copy/paste files until the size reaches size_in_megabytes. This option alone won't erase any file left on destination unless -delete_left_files is also used.
    -shuffle_file_list, shuffles the list of files to copy them randomly. It is useful when used with -size_limit to have a random set of musics under the size limit defined.
    -log, shows all files being copied and deleted.

* You must use .exe extension even running on Linux. It is a peculiarity of standalone export using nuitka I kept.
* Notice that, for now, the only equality check made in -override_on_destination and -delete_left_files is based on the file name.
"""
}

pt = {
    "version": name + " " + version + ": " + codename,
    "invalid path": "Algum dos caminhos recebidos não é uma pasta.",
    "missing required arguments": "Argumentos -source ou -destination faltando. Use ffsmc.exe -h para consultar a ajuda.",
    "missing folder path": "Faltando o caminho da pasta após -source ou -destination. Use ffsmc.exe -h para consultar a ajuda.",
    "invalid size": "Tamanho negativo, não numérico ou não inteiro recebido.",
    "missing size limit": "Faltando tamanho limite após -size_limit. Use ffsmc.exe -h para consultar a ajuda.",
    "scanning source": "Analisando a pasta de origem...",
    "copying new files": "Copiando novos arquivos...",
    "error": "Erro: ",
    "not copied": " não foi copiado.",
    "not deleted": " não foi apagado.",
    "safe exit": "Terminando a execução por segurança.",
    "size limit reached": "Tamanho limite atingido.",
    "copied file not found": "arquivo copiado não encontrado na pasta destino.",
    "deleting left files": "Apagando arquivos restantes...",
    "done": "Feito!",
    "help": name + " " + version + ": " + codename + "\n" +
"""ffsmc.exe -source "pasta_origem" -destination "pasta_destino" [opções]
Opções são:
    -h, mostra esta tela de ajuda.
    -source "pasta_origem", define a pasta de origem na busca por músicas. "pasta_origem" é o caminho da pasta de origem e precisa estar logo após -source. O uso de aspas é recomendado.
    -destination "pasta_destino", define a pasta destino para onde copiar as músicas. "pasta_destino" é o caminho para a pasta destino e deve estar logo após -destination. O uso de aspas é recomendado.
    -override_on_destination, copia todos os arquivos, sobrescrevendo aqueles que já estão no destino. Se não for recebido, será feita a cópia apenas dos arquivos faltando.  
    -delete_left_files, exclui do destino todos os arquivos que não foram encontrados durante a busca, não cumprem os requisitos para seleção (possuir 5 estrelas de rating) ou que não foram copiados por conta do uso de -size_limit. Se não for recebido, eles serão ignorados.
    -size_limit tamanho_em_megabytes, copia arquivos até atingir tamanho_em_megabytes. Esta opção sozinha não apagará arquivos do destino a menos que -delete_left_files também seja usado.
    -shuffle_file_list, embaralha a lista de arquivos a copiar aleatoriamente. É útil em conjunto com -size_limit para ter um conjunto aleatório de músicas abaixo do tamanho limite definido.
    -log, mostra todos os arquivos sendo copiados ou apagados.

* Você deve utilizar a extensão .exe mesmo rodando em Linux. É uma peculiaridade da exportação standalone feita com o nuitka que mantive.
* Note que, por enquanto, a única verificação de igualdade feita em -override_on_destination e -delete_left_files é baseada no nome do arquivo.
"""
}

msg = {
    "en": en,
    "pt": pt
}