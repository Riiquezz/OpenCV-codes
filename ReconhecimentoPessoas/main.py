import getpass
import video
import sys


def main(module):
    video.face_detection_dnn(is_send=False)



def choose_module():
    ans = int(input("""
    Qual módulo executar?
    1 - apenas mostre a imagem da câmera e reconheça as pessoas nela ->  """))

    true_list = [1, 2, 3]

    if ans not in true_list:
        sys.exit("Erro ao inserir o tipo de módulo")
    else:
        return ans


if __name__ == "__main__":
    print("------------------------------------------------------------------------------------------------------"
          "-----------------")
    module_type = choose_module()
    main(module_type)

