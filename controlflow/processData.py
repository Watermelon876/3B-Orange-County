from datetime import datetime
from datetime import timedelta

offenseCodes = {
  11357: 'Possesion of marijuana',
  11358: 'Cultivation of marijuana',
  11359: 'Possesion with intent to sell marijuana',
  11360: 'Sale of marijuana'
}

def getEligibleCases(convictionList):
  return convictionList.filter(isEligible)

def isEligible(conviction):
  currentTime = datetime.now();
  return isEligibleOffense(conviction.penalCode) and
    isTimeServed(conviction.date, conviction.sentenceLength, currentTime)

def isEligibleOffense(penalCode):
  return (penalCode in offenseCodes)

def isTimeServed(date, sentenceLength, dateToday):
  completedTime = date+timedelta(sentenceLength)
