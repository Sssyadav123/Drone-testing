kind: pipeline
name: default

steps:
- name: test
  image: ubuntu
  commands:
  - pwd
  - ls -al

  
