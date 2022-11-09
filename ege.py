def Convert(FromNum,FromBase,ToBase):
    FromNum=int(str(FromNum),FromBase)
    s=''
    while FromNum>0:
        s+=str(FromNum%ToBase)
        FromNum=FromNum//ToBase
    return s[::-1]
