FROM ubuntu
ENV TZ=Asia/Kolkata
WORKDIR /ImSleepy
COPY ./* /ImSleepy/
RUN apt update && apt install -y firefox python3 python3-pip wget tar
RUN pip3 install selenium bs4 2>/dev/null || pip install selenium bs4 2>/dev/null
# CAUTION!!! (UPDATE THIS REGULARLY)
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz"
RUN tar -xvf *gz
RUN mv geckodriver /bin
CMD ["python3 main.py"]
