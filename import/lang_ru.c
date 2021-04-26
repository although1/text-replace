/******************************************************************************
 * * lang_en.c - implementation of language English
 *
 * *(C) Copyright 2019 Asr International Ltd.
 * * All Rights Reserved
 * ******************************************************************************/
#ifndef _LANG_EN_C_
#define _LANG_EN_C_

#include "lv_watch.h"

#if USE_LV_WATCH_LANG_EN != 0

#ifdef __cplusplus
extern "C" {
#endif /* __cpluscplus */

/*********************
*      INCLUDES
*********************/
#include <stdio.h>

const void * lang_text_en[] = {
    /* primary_menu.c */
    "Настройки",
    "Wechat",
    "телефон",
    "Recorder",
    "Camera",
    "Album",
    "Makefriends",
}