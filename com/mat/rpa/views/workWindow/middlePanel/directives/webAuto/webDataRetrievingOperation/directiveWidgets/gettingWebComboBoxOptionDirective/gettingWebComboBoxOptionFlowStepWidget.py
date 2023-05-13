# -*- coding:utf-8 -*-
from com.mat.rpa.views.workWindow.middlePanel.flowPanel import flowStepWidget
from . import gettingWebComboBoxOptionObjectSettingDialog
from ...webDataRetrievingContants import WebDataRetrievingConstants

class GettingWebComboBoxOptionFlowWidget(flowStepWidget.FlowStepWidget):
    def __init__(self, lineNumber, indentLevel, flowTitle, lineNumberWidthSignal, parent=None):
        super(GettingWebComboBoxOptionFlowWidget, self).__init__(lineNumber, indentLevel, flowTitle, lineNumberWidthSignal, parent)
        self.settingDialog = gettingWebComboBoxOptionObjectSettingDialog.GettingWebComboBoxOptionObjectSettingDialog(flowTitle, self)
        self.directive["command"] = WebDataRetrievingConstants.gettingWebElementInfoDirective
        self.directive["data"] = {"web_object": "",
                                  "element": "",
                                  "get_content": 0,
                                  "output": "select_items",
                                  "time_out": "20",
                                  "log": True,
                                  "handle": 0,
                                  "on_error_output_value": "",
                                  "retry_count": 1,
                                  "retry_interval": 1}
        self.infoFormat = u"获取网页%s中%s的%s，将结果保存到%s"
        self.updateSecondLineInfo()

    def getSettingData(self):
        data = self.parent().getDirectiveSettingDataFromDB(self.directive["_id"])
        self.settingDialog.webObjectCombobox.setCurrentText(data["web_object"])
        self.settingDialog.elementLabel.setText(data["element"])
        self.settingDialog.getContentCombobox.setCurrentIndex(data["get_content"])
        self.settingDialog.outputVariableNameLineEdit.setText(data["output"])
        self.settingDialog.waitElementExistLineEdit.setText(data["time_out"])
        self.settingDialog.printErrorLogsCheckbox.setChecked(data["log"])
        self.settingDialog.handleErrorWayCombobox.setCurrentIndex(data["handle"])
        self.settingDialog.onErrorOutputVariableLineEdit.setText(data["on_error_output_value"])
        self.settingDialog.retryCountSpinbox.setValue(data["retry_count"])
        self.settingDialog.retryIntervalSpinbox.setValue(data["retry_interval"])
        self.directive["data"] = data

    def updateSettingData(self):
        data = self.directive["data"]
        data["web_object"] = self.settingDialog.webObjectCombobox.currentText()
        data["element"] = self.settingDialog.elementLabel.text()
        data["get_content"] = self.settingDialog.getContentCombobox.currentIndex()
        data["output"] = self.settingDialog.outputVariableNameLineEdit.text()
        data["time_out"] = self.settingDialog.waitElementExistLineEdit.text()
        data["log"] = self.settingDialog.printErrorLogsCheckbox.isChecked()
        data["handle"] = self.settingDialog.handleErrorWayCombobox.currentIndex()
        data["on_error_output_value"] = self.settingDialog.onErrorOutputVariableLineEdit.text()
        data["retry_count"] = self.settingDialog.retryCountSpinbox.value()
        data["retry_interval"] = self.settingDialog.retryIntervalSpinbox.value()
        self.parent().updateDirectiveData2DB(self.directive["_id"], self.directive["data"])
        self.updateSecondLineInfo()

    def updateSecondLineInfo(self, info: tuple = ()):
        data = self.directive["data"]
        super().updateSecondLineInfo(("${" + data["web_object"] + "}",data["element"],self.settingDialog.getContentCombobox.itemText(data["get_content"]),
                                      "${" + data["output"] + "}"))

