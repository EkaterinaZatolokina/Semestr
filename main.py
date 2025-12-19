import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from database import SportsDatabase


class SportsApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SportsApp, self).__init__()
        uic.loadUi('desk.ui', self)

        self.db = SportsDatabase()
        if not self.db.connect():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных!")
            sys.exit(1)

        self.connect_signals()
        self.load_table_data()

    """Методы для подключения и загрузки первоначальных данных"""
    def connect_signals(self):
        self.loadTableButton.clicked.connect(self.load_table_data)

        self.insertFacilityButton.clicked.connect(self.insert_sports_facility)
        self.updateFacilityButton.clicked.connect(self.update_sports_facility)
        self.deleteFacilityButton.clicked.connect(self.delete_sports_facility)
        self.clearFacilityButton.clicked.connect(self.clear_facility_form)

        self.insertAthleteButton.clicked.connect(self.insert_athlete)
        self.updateAthleteButton.clicked.connect(self.update_athlete)
        self.deleteAthleteButton.clicked.connect(self.delete_athlete)
        self.clearAthleteButton.clicked.connect(self.clear_athlete_form)

        self.insertResultButton.clicked.connect(self.insert_result)
        self.updateResultButton.clicked.connect(self.update_result)
        self.deleteResultButton.clicked.connect(self.delete_result)
        self.clearResultButton.clicked.connect(self.clear_result_form)

        self.loadAuditButton.clicked.connect(self.load_audit_log)
        self.undoButton.clicked.connect(self.undo_operation)
        self.generateReportButton.clicked.connect(self.generate_report)

    def load_table_data(self):
        table_name = self.tableComboBox.currentText()
        try:
            columns, rows = self.db.get_table_data(table_name)

            from PyQt5.QtGui import QStandardItemModel, QStandardItem

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)

            for row in rows:
                items = [QStandardItem(str(item) if item is not None else "") for item in row]
                model.appendRow(items)

            self.tableView.setModel(model)
            self.tableView.resizeColumnsToContents()

            self.statusbar.showMessage(f"Загружено {len(rows)} записей из таблицы {table_name}")

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить данные: {str(e)}")

    """Методы для спортивных сооружений"""
    def insert_sports_facility(self):
        try:
            facility_id = int(self.facilityIdEdit.text())

            query = "SELECT COUNT(*) FROM sports_facility WHERE facility_id = :1"
            self.db.cursor.execute(query, [facility_id])
            count = self.db.cursor.fetchone()[0]

            if count != 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортивное сооружение с ID {facility_id} уже существует!")
                return

            name = self.facilityNameEdit.text()
            facility_type = self.facilityTypeCombo.currentText()

            self.db.insert_sports_facility(facility_id, name, facility_type)
            QMessageBox.information(self, "Успех", "Спортивное сооружение добавлено успешно!")
            self.clear_facility_form()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось добавить сооружение: {str(e)}")

    def update_sports_facility(self):
        try:
            facility_id = int(self.facilityIdEdit.text())

            query = "SELECT COUNT(*) FROM sports_facility WHERE facility_id = :1"
            self.db.cursor.execute(query, [facility_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортивное сооружение с ID {facility_id} не существует!")
                return

            name = self.facilityNameEdit.text() if self.facilityNameEdit.text() else None
            facility_type = self.facilityTypeCombo.currentText()

            self.db.update_sports_facility(facility_id, name, facility_type)
            QMessageBox.information(self, "Успех", "Данные спортивного сооружения обновлены успешно!")

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось обновить сооружение: {str(e)}")

    def delete_sports_facility(self):
        try:
            facility_id = int(self.facilityIdEdit.text())

            query = "SELECT COUNT(*) FROM sports_facility WHERE facility_id = :1"
            self.db.cursor.execute(query, [facility_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортивное сооружение с ID {facility_id} не существует!")
                return

            reply = QMessageBox.question(self, 'Подтверждение',
                                         f'Вы уверены, что хотите удалить спортивное сооружение с ID {facility_id}?',
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.db.delete_sports_facility(facility_id)
                QMessageBox.information(self, "Успех", "Спортивное сооружение удалено успешно!")
                self.clear_facility_form()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось удалить сооружение: {str(e)}")

    def clear_facility_form(self):
        self.facilityIdEdit.clear()
        self.facilityNameEdit.clear()
        self.facilityTypeCombo.setCurrentIndex(0)

    """Методы для спортсменов"""
    def insert_athlete(self):
        try:
            athlete_id = int(self.athleteIdEdit.text())

            query = "SELECT COUNT(*) FROM athlete WHERE athlete_id = :1"
            self.db.cursor.execute(query, [athlete_id])
            count = self.db.cursor.fetchone()[0]

            if count != 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортсмен с ID {athlete_id} уже существует!")
                return

            first_name = self.athleteFirstNameEdit.text()
            last_name = self.athleteLastNameEdit.text()
            birth_date = self.athleteBirthEdit.text() if self.athleteBirthEdit.text() else None

            self.db.insert_athlete(athlete_id, first_name, last_name, birth_date)
            QMessageBox.information(self, "Успех", "Спортсмен добавлен успешно!")
            self.clear_athlete_form()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось добавить спортсмена: {str(e)}")

    def update_athlete(self):
        try:
            athlete_id = int(self.athleteIdEdit.text())

            query = "SELECT COUNT(*) FROM athlete WHERE athlete_id = :1"
            self.db.cursor.execute(query, [athlete_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортсмен с ID {athlete_id} не существует!")
                return

            first_name = self.athleteFirstNameEdit.text() if self.athleteFirstNameEdit.text() else None
            last_name = self.athleteLastNameEdit.text() if self.athleteLastNameEdit.text() else None
            birth_date = self.athleteBirthEdit.text() if self.athleteBirthEdit.text() else None

            self.db.update_athlete(athlete_id, first_name, last_name, birth_date)
            QMessageBox.information(self, "Успех", "Данные спортсмена обновлены успешно!")

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось обновить спортсмена: {str(e)}")

    def delete_athlete(self):
        try:
            athlete_id = int(self.athleteIdEdit.text())

            query = "SELECT COUNT(*) FROM athlete WHERE athlete_id = :1"
            self.db.cursor.execute(query, [athlete_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортсмен с ID {athlete_id} не существует!")
                return

            reply = QMessageBox.question(self, 'Подтверждение',
                                         f'Вы уверены, что хотите удалить спортсмена с ID {athlete_id}?',
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.db.delete_athlete(athlete_id)
                QMessageBox.information(self, "Успех", "Спортсмен удален успешно!")
                self.clear_athlete_form()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось удалить спортсмена: {str(e)}")

    def clear_athlete_form(self):
        self.athleteIdEdit.clear()
        self.athleteFirstNameEdit.clear()
        self.athleteLastNameEdit.clear()
        self.athleteBirthEdit.clear()

    """Методы для результатов соревнований"""
    def insert_result(self):
        try:
            athlete_id = int(self.resultAthleteIdEdit.text())

            query = "SELECT COUNT(*) FROM athlete WHERE athlete_id = :1"
            self.db.cursor.execute(query, [athlete_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Спортсмен с ID {athlete_id} не существует!")
                return

            facility_id = int(self.resultFacilityIdEdit.text()) if self.resultFacilityIdEdit.text() else None
            competition_name = self.resultCompetitionNameEdit.text()
            sport_name = self.resultSportNameEdit.text() if self.resultSportNameEdit.text() else None
            competition_date = self.resultDateEdit.text() if self.resultDateEdit.text() else None
            place = int(self.resultPlaceEdit.text()) if self.resultPlaceEdit.text() else None

            if place and (place <= 0 or place >= 1000):
                QMessageBox.warning(self, "Ошибка", "Место должно быть от 1 до 999!")
                return

            self.db.insert_result(athlete_id, facility_id, competition_name,
                                 sport_name, competition_date, place)
            QMessageBox.information(self, "Успех", "Результат соревнования добавлен успешно!")
            self.clear_result_form()

        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", "Проверьте правильность введенных данных!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось добавить результат: {str(e)}")

    def update_result(self):
        try:
            result_id = int(self.resultIdEdit.text())

            query = "SELECT COUNT(*) FROM competition_result WHERE result_id = :1"
            self.db.cursor.execute(query, [result_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Результат с ID {result_id} не существует!")
                return

            athlete_id = int(self.resultAthleteIdEdit.text()) if self.resultAthleteIdEdit.text() else None
            facility_id = int(self.resultFacilityIdEdit.text()) if self.resultFacilityIdEdit.text() else None
            competition_name = self.resultCompetitionNameEdit.text() if self.resultCompetitionNameEdit.text() else None
            sport_name = self.resultSportNameEdit.text() if self.resultSportNameEdit.text() else None
            competition_date = self.resultDateEdit.text() if self.resultDateEdit.text() else None
            place = int(self.resultPlaceEdit.text()) if self.resultPlaceEdit.text() else None

            if place and (place <= 0 or place >= 1000):
                QMessageBox.warning(self, "Ошибка", "Место должно быть от 1 до 999!")
                return

            self.db.update_result(result_id, athlete_id, facility_id, competition_name,
                                 sport_name, competition_date, place)
            QMessageBox.information(self, "Успех", "Данные результата обновлены успешно!")

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Проверьте правильность введенных данных!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось обновить результат: {str(e)}")

    def delete_result(self):
        try:
            result_id = int(self.resultIdEdit.text())

            query = "SELECT COUNT(*) FROM competition_result WHERE result_id = :1"
            self.db.cursor.execute(query, [result_id])
            count = self.db.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(self, "Предупреждение",
                                    f"Результат с ID {result_id} не существует!")
                return

            reply = QMessageBox.question(self, 'Подтверждение',
                                         f'Вы уверены, что хотите удалить результат с ID {result_id}?',
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.db.delete_result(result_id)
                QMessageBox.information(self, "Успех", "Результат удален успешно!")
                self.clear_result_form()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось удалить результат: {str(e)}")

    def clear_result_form(self):
        self.resultIdEdit.clear()
        self.resultAthleteIdEdit.clear()
        self.resultFacilityIdEdit.clear()
        self.resultCompetitionNameEdit.clear()
        self.resultSportNameEdit.clear()
        self.resultDateEdit.clear()
        self.resultPlaceEdit.clear()

    """Методы для логов"""
    def load_audit_log(self):
        try:
            start_date = self.startDateEdit.text() if self.startDateEdit.text() else None
            end_date = self.endDateEdit.text() if self.endDateEdit.text() else None
            operation_type = self.operationTypeCombo.currentText()
            operation_type = None if operation_type == "Все" else operation_type

            result = self.db.get_audit_log(start_date, end_date, operation_type)

            if result:
                columns, rows = result

                from PyQt5.QtGui import QStandardItemModel, QStandardItem

                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(columns)

                for row in rows:
                    items = [QStandardItem(str(item) if item is not None else "") for item in row]
                    model.appendRow(items)

                self.auditTableView.setModel(model)
                self.auditTableView.resizeColumnsToContents()

                self.statusbar.showMessage(f"Загружено {len(rows)} записей из лога")
            else:
                QMessageBox.information(self, "Информация", "Нет данных для отображения")

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить лог: {str(e)}")

    def undo_operation(self):
        try:
            log_id = int(self.undoIdEdit.text())

            reply = QMessageBox.question(self, 'Подтверждение',
                                         f'Вы уверены, что хотите отменить операцию с ID {log_id}?',
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.db.undo_operation(log_id)
                QMessageBox.information(self, "Успех", "Операция отменена успешно!")
                self.undoIdEdit.clear()

                self.load_audit_log()
                self.load_table_data()

                current_table = self.tableComboBox.currentText()
                if current_table != 'audit_log':
                    self.load_table_data()

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "ID должен быть числом!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось отменить операцию: {str(e)}")

    """Метод для отчетов"""
    def generate_report(self):
        try:
            flag1 = self.flag1CheckBox.isChecked()
            flag2 = self.flag2CheckBox.isChecked()
            flag3 = self.flag3CheckBox.isChecked()

            result = self.db.get_summary_report(flag1, flag2, flag3)

            if result:
                columns, rows = result

                from PyQt5.QtGui import QStandardItemModel, QStandardItem

                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(columns)

                for row in rows:
                    items = [QStandardItem(str(item) if item is not None else "") for item in row]
                    model.appendRow(items)

                self.reportTableView.setModel(model)
                self.reportTableView.resizeColumnsToContents()

                self.statusbar.showMessage(f"Сгенерирован отчет на {len(rows)} строк")
            else:
                QMessageBox.information(self, "Информация", "Нет данных для отображения")

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось сгенерировать отчет: {str(e)}")

    def closeEvent(self, event):
        self.db.disconnect()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SportsApp()
    window.show()
    sys.exit(app.exec_())