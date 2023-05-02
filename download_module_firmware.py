import os
import subprocess

def rmtree(top):
    import stat
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)

root = os.path.dirname(__file__)
s3_path = 's3://luxrobo-download/release-modi2-firmware/module_firmware'
module_firmware_path = os.path.join(root, "module_firmware")

# create dir
if os.path.exists(module_firmware_path):
    rmtree(module_firmware_path)
os.mkdir(module_firmware_path)

# download
subprocess.run(['aws', 's3', 'cp', s3_path, module_firmware_path, '--recursive'])
