## Review Project

# 설명
사용자가 음악, 영화, 책에 대한 리뷰를 등록, 수정하고 여러개의 리뷰를 각각의 주제에 맞추어 리스트를 만들 수 있는 사이트입니다.

# 기술 스택
- Backend: Python, Django
- Database: MySQL
- Frontend: HTML, CSS

# 주요 기능
- 리뷰 작성 / 수정 / 삭제
- 리뷰 리스트 생성

# 실행
git clone https://github.com/hajin0829/my-list-project.git
cd my-list-project

python -m venv venv
venv\Scripts\activate

pip install django
pip install mysqlclient
pip install Pillow

cd review_project
python manage.py migrate

python manage.py runserver

