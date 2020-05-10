from application import application
from flask import flash, request
import sqlhelper

@application.route('/projectfunder', methods=['POST'])
def projectfunder_add():
    try:
        content = request.json
        _projectid = content['ProjectId']
        _categoryid = content['FunderId']
        _amount = content['AmountFunded']

        sql = "CALL usp_AddFunderToProject(%s, %s, %s)"
        data = (_projectid, _categoryid, _amount,)
        resp = sqlhelper.do_writedata(sql, data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)        

@application.route('/projectfunder/<int:id>', methods=['DELETE'])
def delete_projectfunder(id):
    try:
        sql = "CALL usp_RemoveFunderFromProject(%s)"
        data = (id,)
        resp = sqlhelper.do_writedata(sql, data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@application.route('/projectfunder/<int:projectid>', methods=['GET'])
def projectfunder(projectid):
    try:
        resp = sqlhelper.do_selectmultibyid("CALL usp_GetFundersForProject(%s)", projectid)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)