kind: pipeline
name: default

steps:
- name: test
  image: ubuntu
  commands:
  - cd /usr/local/bin/dockerd
  - pwd
  - ls

  
