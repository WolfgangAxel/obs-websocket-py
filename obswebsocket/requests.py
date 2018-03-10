#!/usr/bin/env python
# -*- coding: utf-8 -*-

### THIS FILE WAS GENERATED BY ./generate_classes.py - DO NOT EDIT ###

from . import base_classes

class GetVersion(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetVersion"
        self.datain["version"] = None
        self.datain["obs-websocket-version"] = None
        self.datain["obs-studio-version"] = None

    def getVersion(self):
        return self.datain["version"]

    def getObsWebsocketVersion(self):
        return self.datain["obs-websocket-version"]

    def getObsStudioVersion(self):
        return self.datain["obs-studio-version"]


class GetAuthRequired(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetAuthRequired"
        self.datain["challenge"] = None
        self.datain["salt"] = None

    def getChallenge(self):
        return self.datain["challenge"]

    def getSalt(self):
        return self.datain["salt"]


class Authenticate(base_classes.Baserequests):
    def __init__(self, auth):
        base_classes.Baserequests.__init__(self)
        self.name = "Authenticate"
        self.dataout["auth"] = auth


class GetCurrentScene(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetCurrentScene"
        self.datain["name"] = None
        self.datain["sources"] = None

    def getName(self):
        return self.datain["name"]

    def getSources(self):
        return self.datain["sources"]


class SetCurrentScene(base_classes.Baserequests):
    def __init__(self, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetCurrentScene"
        self.dataout["scene-name"] = scene_name


class GetSceneList(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetSceneList"
        self.datain["current-scene"] = None
        self.datain["scenes"] = None

    def getCurrentScene(self):
        return self.datain["current-scene"]

    def getScenes(self):
        return self.datain["scenes"]


class SetSourceRender(base_classes.Baserequests):
    def __init__(self, source, render, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetSourceRender"
        self.dataout["source"] = source
        self.dataout["render"] = render
        self.dataout["scene-name"] = scene_name


class GetStudioModeStatus(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetStudioModeStatus"
        self.datain["studio-mode"] = None

    def getStudioMode(self):
        return self.datain["studio-mode"]


class GetPreviewScene(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetPreviewScene"


class SetPreviewScene(base_classes.Baserequests):
    def __init__(self, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetPreviewScene"
        self.dataout["scene-name"] = scene_name


class TransitionToProgram(base_classes.Baserequests):
    def __init__(self, with_transition):
        base_classes.Baserequests.__init__(self)
        self.name = "TransitionToProgram"
        self.datain["name"] = None
        self.datain["duration"] = None
        self.dataout["with-transition"] = with_transition

    def getName(self):
        return self.datain["name"]

    def getDuration(self):
        return self.datain["duration"]


class EnableStudioMode(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "EnableStudioMode"


class DisableStudioMode(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "DisableStudioMode"


class ToggleStudioMode(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "ToggleStudioMode"


class StartStopStreaming(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "StartStopStreaming"


class StartStopRecording(base_classes.Baserequests):
    def __init__(self, stream):
        base_classes.Baserequests.__init__(self)
        self.name = "StartStopRecording"
        self.dataout["stream"] = stream


class StartStreaming(base_classes.Baserequests):
    def __init__(self, stream, settings, type, metadata, server, key, use_auth, username, password):
        base_classes.Baserequests.__init__(self)
        self.name = "StartStreaming"
        self.dataout["stream"] = stream
        self.dataout["settings"] = settings
        self.dataout["type"] = type
        self.dataout["metadata"] = metadata
        self.dataout["server"] = server
        self.dataout["key"] = key
        self.dataout["use-auth"] = use_auth
        self.dataout["username"] = username
        self.dataout["password"] = password


class StopStreaming(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "StopStreaming"


class StartRecording(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "StartRecording"


class StopRecording(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "StopRecording"


class SetRecordingFolder(base_classes.Baserequests):
    def __init__(self, rec_folder):
        base_classes.Baserequests.__init__(self)
        self.name = "SetRecordingFolder"
        self.dataout["rec-folder"] = rec_folder


class GetRecordingFolder(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetRecordingFolder"
        self.datain["rec-folder"] = None

    def getRecFolder(self):
        return self.datain["rec-folder"]


class GetStreamingStatus(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetStreamingStatus"
        self.datain["streaming"] = None
        self.datain["recording"] = None
        self.datain["stream-timecode"] = None
        self.datain["rec-timecode"] = None
        self.datain["preview-only"] = None

    def getStreaming(self):
        return self.datain["streaming"]

    def getRecording(self):
        return self.datain["recording"]

    def getStreamTimecode(self):
        return self.datain["stream-timecode"]

    def getRecTimecode(self):
        return self.datain["rec-timecode"]

    def getPreviewOnly(self):
        return self.datain["preview-only"]


class GetTransitionList(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetTransitionList"
        self.datain["current-transition"] = None
        self.datain["transitions"] = None

    def getCurrentTransition(self):
        return self.datain["current-transition"]

    def getTransitions(self):
        return self.datain["transitions"]


class GetCurrentTransition(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetCurrentTransition"
        self.datain["name"] = None
        self.datain["duration"] = None

    def getName(self):
        return self.datain["name"]

    def getDuration(self):
        return self.datain["duration"]


class SetCurrentTransition(base_classes.Baserequests):
    def __init__(self, transition_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetCurrentTransition"
        self.dataout["transition-name"] = transition_name


class SetTransitionDuration(base_classes.Baserequests):
    def __init__(self, duration):
        base_classes.Baserequests.__init__(self)
        self.name = "SetTransitionDuration"
        self.dataout["duration"] = duration


class GetTransitionDuration(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetTransitionDuration"
        self.datain["transition-duration"] = None

    def getTransitionDuration(self):
        return self.datain["transition-duration"]


class SetVolume(base_classes.Baserequests):
    def __init__(self, source, volume):
        base_classes.Baserequests.__init__(self)
        self.name = "SetVolume"
        self.dataout["source"] = source
        self.dataout["volume"] = volume


class GetVolume(base_classes.Baserequests):
    def __init__(self, source):
        base_classes.Baserequests.__init__(self)
        self.name = "GetVolume"
        self.datain["name"] = None
        self.datain["volume"] = None
        self.datain["muted"] = None
        self.dataout["source"] = source

    def getName(self):
        return self.datain["name"]

    def getVolume(self):
        return self.datain["volume"]

    def getMuted(self):
        return self.datain["muted"]


class SetMute(base_classes.Baserequests):
    def __init__(self, source, mute):
        base_classes.Baserequests.__init__(self)
        self.name = "SetMute"
        self.dataout["source"] = source
        self.dataout["mute"] = mute


class GetMute(base_classes.Baserequests):
    def __init__(self, source):
        base_classes.Baserequests.__init__(self)
        self.name = "GetMute"
        self.datain["name"] = None
        self.datain["muted"] = None
        self.dataout["source"] = source

    def getName(self):
        return self.datain["name"]

    def getMuted(self):
        return self.datain["muted"]


class ToggleMute(base_classes.Baserequests):
    def __init__(self, source):
        base_classes.Baserequests.__init__(self)
        self.name = "ToggleMute"
        self.dataout["source"] = source


class GetSpecialSources(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetSpecialSources"
        self.datain["desktop-1"] = None
        self.datain["desktop-1"] = None
        self.datain["mic-1"] = None
        self.datain["mic-2"] = None
        self.datain["mic-3"] = None

    def getDesktop1(self):
        return self.datain["desktop-1"]

    def getDesktop1(self):
        return self.datain["desktop-1"]

    def getMic1(self):
        return self.datain["mic-1"]

    def getMic2(self):
        return self.datain["mic-2"]

    def getMic3(self):
        return self.datain["mic-3"]


class SetSceneItemPosition(base_classes.Baserequests):
    def __init__(self, item, x, y, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetSceneItemPosition"
        self.dataout["item"] = item
        self.dataout["x"] = x
        self.dataout["y"] = y
        self.dataout["scene-name"] = scene_name


class SetSceneItemTransform(base_classes.Baserequests):
    def __init__(self, item, x_scale, y_scale, rotation, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetSceneItemTransform"
        self.dataout["item"] = item
        self.dataout["x-scale"] = x_scale
        self.dataout["y-scale"] = y_scale
        self.dataout["rotation"] = rotation
        self.dataout["scene-name"] = scene_name


class SetSceneItemCrop(base_classes.Baserequests):
    def __init__(self, item, scene_name, top, bottom, left, right):
        base_classes.Baserequests.__init__(self)
        self.name = "SetSceneItemCrop"
        self.dataout["item"] = item
        self.dataout["scene-name"] = scene_name
        self.dataout["top"] = top
        self.dataout["bottom"] = bottom
        self.dataout["left"] = left
        self.dataout["right"] = right


class SetCurrentSceneCollection(base_classes.Baserequests):
    def __init__(self, sc_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetCurrentSceneCollection"
        self.dataout["sc-name"] = sc_name


class GetCurrentSceneCollection(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetCurrentSceneCollection"
        self.datain["sc-name"] = None

    def getScName(self):
        return self.datain["sc-name"]


class ListSceneCollections(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "ListSceneCollections"
        self.datain["scene-collections"] = None

    def getSceneCollections(self):
        return self.datain["scene-collections"]


class SetStreamSettings(base_classes.Baserequests):
    def __init__(self, type, settings, save, server, key, use_auth, username, password):
        base_classes.Baserequests.__init__(self)
        self.name = "SetStreamSettings"
        self.datain["type"] = None
        self.datain["settings"] = None
        self.datain["server"] = None
        self.datain["key"] = None
        self.datain["use-auth"] = None
        self.datain["username"] = None
        self.datain["password"] = None
        self.dataout["type"] = type
        self.dataout["settings"] = settings
        self.dataout["save"] = save
        self.dataout["server"] = server
        self.dataout["key"] = key
        self.dataout["use-auth"] = use_auth
        self.dataout["username"] = username
        self.dataout["password"] = password

    def getType(self):
        return self.datain["type"]

    def getSettings(self):
        return self.datain["settings"]

    def getServer(self):
        return self.datain["server"]

    def getKey(self):
        return self.datain["key"]

    def getUseAuth(self):
        return self.datain["use-auth"]

    def getUsername(self):
        return self.datain["username"]

    def getPassword(self):
        return self.datain["password"]


class SetCurrentProfile(base_classes.Baserequests):
    def __init__(self, profile_name):
        base_classes.Baserequests.__init__(self)
        self.name = "SetCurrentProfile"
        self.dataout["profile-name"] = profile_name


class GetCurrentProfile(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "GetCurrentProfile"
        self.datain["profile-name"] = None

    def getProfileName(self):
        return self.datain["profile-name"]


class ListProfiles(base_classes.Baserequests):
    def __init__(self):
        base_classes.Baserequests.__init__(self)
        self.name = "ListProfiles"
        self.datain["profiles"] = None

    def getProfiles(self):
        return self.datain["profiles"]


class GetSourceSettings(base_classes.Baserequests):
    def __init__(self, source, source_type):
        base_classes.Baserequests.__init__(self)
        self.name = "GetSourceSettings"
        self.datain["sourceSettings"] = None
        self.dataout["sourceName"] = source
        self.dataout["sourceType"] = source_type
    
    def getSettings(self):
        return self.datain['sourceSettings']

class SetSourceSettings(base_classes.Baserequests):
    def __init__(self, source, source_type, settings):
        base_classes.Baserequests.__init__(self)
        self.name = "SetSourceSettings"
        self.dataout["sourceName"] = source
        self.dataout["sourceType"] = source_type
        self.dataout['sourceSettings'] = settings


class GetTextGDIPlusProperties(base_classes.Baserequests):
    def __init__(self, source, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "GetTextGDIPlusProperties"
        self.datain["align"] = None
        self.datain["chatlog"] = None
        self.datain["color"] = None
        self.datain["extents"] = None
        self.datain["file"] = None
        self.datain["font"] = None
        self.datain["face"] = None
        self.datain["flags"] = None
        self.datain["size"] = None
        self.datain["style"] = None
        self.datain["gradient"] = None
        self.datain["outline"] = None
        self.datain["text"] = None
        self.datain["valign"] = None
        self.datain["vertical"] = None
        self.datain["render"] = None
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name

    def getAlign(self):
        return self.datain["align"]

    def getChatlog(self):
        return self.datain["chatlog"]

    def getColor(self):
        return self.datain["color"]

    def getExtents(self):
        return self.datain["extents"]

    def getFile(self):
        return self.datain["file"]

    def getFont(self):
        return self.datain["font"]

    def getFace(self):
        return self.datain["face"]

    def getFlags(self):
        return self.datain["flags"]

    def getSize(self):
        return self.datain["size"]

    def getStyle(self):
        return self.datain["style"]

    def getGradient(self):
        return self.datain["gradient"]

    def getOutline(self):
        return self.datain["outline"]

    def getText(self):
        return self.datain["text"]

    def getValign(self):
        return self.datain["valign"]

    def getVertical(self):
        return self.datain["vertical"]

    def getRender(self):
        return self.datain["render"]


class SetTextGDIPlusProperties(base_classes.Baserequests):
    def __init__(self, source, scene_name, align, chatlog, color, extents, file, font, face, flags, size, style, gradient, outline, text, valign, vertical, render):
        base_classes.Baserequests.__init__(self)
        self.name = "SetTextGDIPlusProperties"
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name
        self.dataout["align"] = align
        self.dataout["chatlog"] = chatlog
        self.dataout["color"] = color
        self.dataout["extents"] = extents
        self.dataout["file"] = file
        self.dataout["font"] = font
        self.dataout["face"] = face
        self.dataout["flags"] = flags
        self.dataout["size"] = size
        self.dataout["style"] = style
        self.dataout["gradient"] = gradient
        self.dataout["outline"] = outline
        self.dataout["text"] = text
        self.dataout["valign"] = valign
        self.dataout["vertical"] = vertical
        self.dataout["render"] = render


class GetTextFreetype2Properties(base_classes.Baserequests):
    def __init__(self, source, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "GetTextFreetype2Properties"
        self.datain["color1"] = None
        self.datain["color2"] = None
        self.datain["custom_width"] = None
        self.datain["drop_shadow"] = None
        self.datain["font"] = {'face': None, 'flags': None, 'size': None, 'style': None}
        self.datain["from_file"] = None
        self.datain["log_mode"] = None
        self.datain["outline"] = None
        self.datain["text"] = None
        self.datain["text_file"] = None
        self.datain["word_wrap"] = None
        self.datain["render"] = None
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name

    def getColor1(self):
        return self.datain["color1"]
        
    def getColor2(self):
        return self.datain["color2"]
        
    def getCustomwidth(self):
        return self.datain["custom_width"]
        
    def getDropshadow(self):
        return self.datain["drop_shadow"]
        
    def getFont(self):
        return self.datain["font"]
        
    def getFace(self):
        return self.datain["font"]["face"]
        
    def getFlags(self):
        return self.datain["font"]["flags"]
        
    def getSize(self):
        return self.datain["font"]["size"]
        
    def getStyle(self):
        return self.datain["font"]["style"]
        
    def getFromfile(self):
        return self.datain["from_file"]
        
    def getLogmode(self):
        return self.datain["log_mode"]
        
    def getOutline(self):
        return self.datain["outline"]
        
    def getText(self):
        return self.datain["text"]
        
    def getTextfile(self):
        return self.datain["text_file"]
        
    def getWordwrap(self):
        return self.datain["word_wrap"]
        
    def getRender(self):
        return self.datain["render"]


class SetTextFreetype2Properties(base_classes.Baserequests):
    def __init__(self, source, scene_name, color1, color2, custom_width, drop_shadow, font, from_file, log_mode, outline, text, text_file, word_wrap, render):
        base_classes.Baserequests.__init__(self)
        self.name = "SetTextFreetype2Properties"
        self.dataout["color1"] = color1
        self.dataout["color2"] = color2
        self.dataout["custom_width"] = custom_width
        self.dataout["drop_shadow"] = drop_shadow
        self.dataout["font"] = font
        self.dataout["from_file"] = from_file
        self.dataout["log_mode"] = log_mode
        self.dataout["outline"] = outline
        self.dataout["text"] = text
        self.dataout["text_file"] = text_file
        self.dataout["word_wrap"] = word_wrap
        self.dataout["render"] = render
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name

class GetBrowserSourceProperties(base_classes.Baserequests):
    def __init__(self, source, scene_name):
        base_classes.Baserequests.__init__(self)
        self.name = "GetBrowserSourceProperties"
        self.datain["url"] = None
        self.datain["css"] = None
        self.datain["width"] = None
        self.datain["height"] = None
        self.datain["fps"] = None
        self.datain["shutdown"] = None
        self.datain["render"] = None
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name

    def getUrl(self):
        return self.datain["url"]

    def getCss(self):
        return self.datain["css"]

    def getWidth(self):
        return self.datain["width"]

    def getHeight(self):
        return self.datain["height"]

    def getFps(self):
        return self.datain["fps"]

    def getShutdown(self):
        return self.datain["shutdown"]

    def getRender(self):
        return self.datain["render"]


class SetBrowserSourceProperties(base_classes.Baserequests):
    def __init__(self, source, scene_name, url, css, width, height, fps, shutdown, render):
        base_classes.Baserequests.__init__(self)
        self.name = "SetBrowserSourceProperties"
        self.dataout["source"] = source
        self.dataout["scene-name"] = scene_name
        self.dataout["url"] = url
        self.dataout["css"] = css
        self.dataout["width"] = width
        self.dataout["height"] = height
        self.dataout["fps"] = fps
        self.dataout["shutdown"] = shutdown
        self.dataout["render"] = render


