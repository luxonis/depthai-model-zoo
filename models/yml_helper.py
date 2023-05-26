from pathlib import Path
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-folder', '--folder', type=str, help="Folder path where you have IR model stored (.bin and .xml)")
args = parser.parse_args()

def sha384sum(filename: Path):
    h  = hashlib.sha384()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(str(filename.resolve()), 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def sha256sum(filename: Path):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(str(filename.resolve()), 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


xmls =  list(Path(args.folder).glob('*.xml'))
bins =  list(Path(args.folder).glob('*.bin'))

if len(xmls) == 0 or len(bins) == 0:
    raise Exception('Specified folder does not contain xml and bin file!')

xml = Path(xmls[0])
bin = Path(bins[0])

print(xml, bin)

if xml.stem != bin.stem:
    raise Exception('xml and bin file names should be the same!')


with open(str(Path(args.folder) / "model.yml"), "w") as yml:
    yml.write(f"""description: empty
license: empty
task_type: object_attributes
files:
- checksum: {sha384sum(xml)}
  name: FP16/{xml.name}
  sha256: {sha256sum(xml)}
  size: {xml.stat().st_size}
  source: https://github.com/luxonis/depthai-model-zoo/raw/main/models/{xml.stem}/{xml.name}
- checksum: {sha384sum(bin)}
  name: FP16/{bin.name}
  sha256: {sha256sum(bin)}
  size: {bin.stat().st_size}
  source: https://robothub.fra1.cdn.digitaloceanspaces.com/models/{bin.stem}/{bin.name}
framework: dldt
""")