SHELL := /bin/bash
BASEDIR = $(shell pwd)

APP_VERSION := 1.0.0
IMAGE_NAME = "hcylus/$(APP_NAME):$(APP_VERSION)"
IMAGE_LATEST = "hcylus/$(APP_NAME):latest"
SUBDIR := $(shell find $(BASEDIR)/ -maxdepth 1 -path $(BASEDIR)/.git -prune -o -type d -print)
DIRLIST := $(notdir $(SUBDIR))

ifeq (image,$(firstword $(MAKECMDGOALS)))
	RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
	# RUN_ARGS := $(filter-out $@,$(MAKECMDGOALS))
# %: 匹配任何名称的target; @: 空recipe=什么也不做
# %:
# 	@:
  $(eval $(RUN_ARGS):;@:)
endif

ifdef RUN_ARGS
	APPLIST := $(RUN_ARGS)
else
	APPLIST := $(DIRLIST)
endif


.PHONY: all
image: $(APPLIST)
	$(info imagelist: $(APPLIST))
	@$(foreach APP_NAME,$(APPLIST),\
		$(if $(wildcard $(BASEDIR)/$(APP_NAME)/Dockerfile),\
			echo start build image $(IMAGE_NAME);\
			cd $(BASEDIR)/$(APP_NAME);\
			docker build -t $(IMAGE_NAME) -f Dockerfile . || exit $$?;\
			echo build image $(IMAGE_NAME) done;\
			docker tag $(IMAGE_NAME) $(IMAGE_LATEST);\
			docker push $(IMAGE_NAME);\
			docker push $(IMAGE_LATEST);\
			echo,\
			$(warning $(APP_NAME) not exist Dockerfile)\
		)\
	)

help:
	@echo "image - build and push image to docker"
