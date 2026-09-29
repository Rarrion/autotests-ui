import platform
import sys

from config import settings


def create_allure_environment_file():
    # Формируем строки в формате {key}={value} из всех настроек проекта
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Добавляем информацию об операционной системе и версии Python
    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
