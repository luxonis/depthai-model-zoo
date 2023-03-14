from pathlib import Path
import hashlib
import argparse
import yaml
from typing import Optional


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--fp16',
        type=Path,
        help='Path to FP16 xml file'
    )
    parser.add_argument(
        '--int8',
        type=Path,
        help='Path to INT8 xml file',
        required=False,
        default=None
    )
    parser.add_argument(
        '--desc',
        type=str,
        required=False,
        default=None,
        help='Description of the model'
    )
    parser.add_argument(
        '--license',
        type=str,
        required=False,
        default=None,
        help='License of the model'
    )
    parser.add_argument(
        '--task_type',
        required=False,
        default='object_attributes',
        help='Task type of the model'
    )
    parser.add_argument(
        '--framework',
        required=False,
        default='dldt',
        help='Framework of the model'
    )
    parser.add_argument(
        '--destination',
        required=False,
        type=Path,
        default=Path.cwd(),
        help='Destination folder for model.yml'
    )

    return parser.parse_args()


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


def make_file_record(file: Path, is_int8=False):
    name_prefix = 'FP16-INT8' if is_int8 else 'FP16'

    if file.suffix == '.xml':
        source = f'https://github.com/luxonis/depthai-model-zoo/raw/main/models/{file.stem}/{file.name}'
    else:
        source = 'EDIT'

    return {
        'checksum': sha384sum(file),
        'name': f'{name_prefix}/{file.name}',
        'sha256': sha256sum(file),
        'size': file.stat().st_size,
        'source': source
    }


def make_yaml_string(xml_16: Path,
                     bin_16: Path,
                     xml_8: Optional[Path] = None,
                     bin_8: Optional[Path] = None,
                     *,
                     desc: Optional[str] = None,
                     license: Optional[str] = None,
                     task_type: str = 'object_attributes',
                     framework: str = 'dldt'):

    files = [make_file_record(xml_16), make_file_record(bin_16)]

    if xml_8 is not None and bin_8 is not None:
        files.append(make_file_record(xml_8, is_int8=True))
        files.append(make_file_record(bin_8, is_int8=True))

    yaml_dict = {
        'description': desc or 'empty',
        'license': license or 'empty',
        'task_type': task_type,
        'files': files,
        'framework': framework,
    }

    return yaml.dump(yaml_dict, stream=None)


def main():
    args = get_args()
    xml_16 = args.fp16
    bin_16 = args.fp16.with_suffix('.bin')
    xml_8 = args.int8
    bin_8 = args.int8.with_suffix('.bin') if args.int8 is not None else None

    if not xml_16.exists() or not bin_16.exists():
        raise FileNotFoundError('FP16 xml or bin file does not exist!')

    if xml_8 is not None and bin_8 is not None:
        if not xml_8.exists() or not bin_8.exists():
            raise FileNotFoundError('INT8 xml or bin file does not exist!')

    with open(str(Path(args.destination) / 'model.yml'), 'w') as yml:
        yml.write(make_yaml_string(xml_16, bin_16,
                                   xml_8, bin_8,
                                   desc=args.desc,
                                   license=args.license,
                                   task_type=args.task_type,
                                   framework=args.framework))


if __name__ == '__main__':
    main()
