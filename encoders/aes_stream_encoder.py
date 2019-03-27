import library.modules.config as config
import base64

config.main()


def main(option, filepath=None):
    if not filepath:
        filepath = config.scout_values['Path'][0]
    if option == 'encode':
        try:
            imported_modules = ['from Crypto.Cipher import AES', 'import base64']
            with open(filepath, 'r') as f:
                data = f.read().replace(';', '\n')
            source = data.split('\n')
            for i in source:
                if 'import' in i and i != 'from Crypto.Cipher import AES':
                    imported_modules.append(i)
            obfuscated = ';'.join(imported_modules) + ';exec(base64.b64decode("' + base64.b64encode('\n'.join(source)) + '"))'
            with open(filepath, 'w') as f:
                f.write(obfuscated)
                print '   ' + config.inf + 'Encoded scout and overwrote raw file with AES stream cipher encrypted file contents'
        except SyntaxError:
            print '   ' + config.neg + 'Could not encode scout'
    elif option == 'info':
        print '\nName             : AES Encoder' \
              '\nRequired Modules : pycryptodome' \
              '\nDescription      : Uses the AES stream cipher to symmetrically encrypt the scout\n'
