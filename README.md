# 전주비전대 Project 

## Install DHT11 sensor 
```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
cd Adafruit_Python_DHT
sudo python setup.py install
cd Adafruit_Python_DHT/examples
```
  - run
  ```
  python AdafruitDHT.py 11 4
  ```
## JAVA Install

## OpenTSDB Install
```
cd /usr/local
sudo wget http://mirror.23media.de/apache/hbase/2.1.1/hbase-2.1.1-bin.tar.gz
sudo tar xzvf hbase-2.1.1-bin.tar.gz
cd hbase-2.1.1
```
### OpenTSDB 환경 설정
`sudo vim conf/hbase-env.sh` 에서 `JAVA_HOME=/usr` 로 수정

`sudo vim conf/hbase-site.xml` 에서 다음처럼 내용을 추가
```xml
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file:///var/local/hbase-2.1.1/hbase</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>/var/local/hbase-2.1.1/zookeeper</value>
  </property>
  <property>
    <name>hbase.unsafe.stream.capability.enforce</name>
    <value>false</value>
    <description>
      Controls whether HBase will check for stream capabilities (hflush/hsync).

      Disable this if you intend to run on LocalFileSystem, denoted by a rootdir
      with the 'file://' scheme, but be mindful of the NOTE below.

      WARNING: Setting this to false blinds you to potential data loss and
      inconsistent system state in the event of process and/or node failures. If
      HBase is complaining of an inability to use hsync or hflush it's most
      likely not a false positive.
    </description>
  </property>
</configuration>
```
  - run program
  ```
  sudo ./bin/start-hbase.sh
  ```
## 필요 패키지 설치
```
sudo apt update
sudo apt install gnuplot
sudo apt update
sudo apt install autotools-dev
sudo apt update
sudo apt install autoconf
sudo apt update
sudo apt install make
sudo apt update
sudo apt install python
sudo apt update
sudo apt install python3
sudo apt update
sudo apt install git
```
## OPEN TSDB 프로그램 다운로드 및 빌드
```
cd /usr/local
sudo git clone git://github.com/OpenTSDB/opentsdb.git
cd opentsdb
sudo ./build.sh
```

# InfluxDB Installation

## 1. Repository의 GPG key를 더하기
```
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```

## 2. Repository를 더하기
```
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

## 3. 프로그램 설치
```
sudo apt update
sudo apt install influxdb
```

## 4. 프로그램 실행
```
sudo service influxdb start
```

# Grafana Installation

## 1. Repository의 GPG key를 더하기
```
curl https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
```

## 2. Repository를 더하기
```
echo "deb https://dl.bintray.com/fg2it/deb stretch main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

## 3. 프로그램 설치
```
sudo apt update
sudo apt install grafana
```

## 4. 프로그램 실행
```
sudo service grafana-server start
```
## influxdb import with python
```
sudo pip install influxdb
```
## gpio pin map
```
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
```
