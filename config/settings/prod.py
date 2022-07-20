from .base import *

# 서버 환경을 담당
ALLOWED_HOSTS = ['13.209.252.184']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = [] # STATICFILES_DIRS의 리스트에 STATIC_ROOT와 동일한 디렉터리 포함되어 있으면 오류나는 걸 방지
DEBUG = False