from sqlalchemy import Column, String, Integer, SmallInteger, BigInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy, Model
from flask import current_app
from datetime import datetime

db = SQLAlchemy(current_app)

# 会员
class User(Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) # 编号
    name = Column(String(100), unique=True) # 昵称
    pwd = Column(String(100))   # 密码
    email = Column(String(100),unique=True) # 邮箱
    phone = Column(String(11), unique=True) # 手机号
    info = Column(Text) # 个人简介
    face = Column(String(255), unique=True) # 头像
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间
    uuid = Column(String(255), unique=True) # 唯一标志符
    userlogs = relationship('Userlog', backref='user') # 会员日志外键关系关联
    comment = relationship('Comment', backref='user')   # 评论外键关系关联
    moviecols = relationship('Moviecol', backref='user')   # 收藏外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name


# 会员登录日志
class Userlog(Model):
    __tablename__ = 'userlog'
    id = Column(Integer, primary_key=True) # 编号
    user_id = Column(Integer, ForeignKey('user.id')) # 所属会员
    ip = Column(String(100))    # ip地址
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Userlog %r>' % self.id

# 标签
class Tag(Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True) # 编号
    name = Column(String(255), unique=True)  # 标题
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间
    movies = relationship('Movie', backref='tag') # 电影外键关系关联

    def __repr__(self):
        return '<Tag %r>' % self.name

# 电影
class Movie(Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True) # 编号
    title = Column(String(255), unique=True)  # 标题
    url = Column(String(255), unique=True)  # 地址
    info = Column(Text) # 简介
    logo = Column(String(255), unique=True)  # 封面
    star = Column(SmallInteger)  # 星级
    playnum = Column(BigInteger) # 播放量
    commentnum = Column(BigInteger) # 评论量
    tag_id = Column(Integer, ForeignKey('tag.id')) # 所属标签
    area = Column(String(255)) # 上映地区
    release_time = Column(DateTime)    # 上映时间
    length = Column(String(100))    # 播放时间
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间
    comments = relationship('Comment', backref='movie') # 评论外键关系关联
    moviecols = relationship('Moviecol', backref='movie') # 收藏外键关系关联

    def __repr__(self):
        return '<Tag %r>' % self.title

# 上映预告
class Preview(Model):
    __tablename__ = 'preview'
    id = Column(Integer, primary_key=True)  # 编号
    title = Column(String(255), unique=True)  # 标题
    logo = Column(String(255), unique=True)  # 封面
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Preview %r>' % self.title


# 评论
class Comment(Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)  # 编号
    content = Column(Text) # 内容
    movie_id = Column(Integer, ForeignKey('movie.id')) # 所属电影
    user_id = Column(Integer, ForeignKey('user.id')) # 所属用户
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Comment %r>' % self.id


# 电影收藏
class Moviecol(Model):
    __tablename__ = 'moviecol'
    id = Column(Integer, primary_key=True)  # 编号
    content = Column(Text) # 内容
    movie_id = Column(Integer, ForeignKey('movie.id')) # 所属电影
    user_id = Column(Integer, ForeignKey('user.id')) # 所属用户
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Moviecol %r>' % self.id


# 权限
class Auth(Model):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True)  # 编号
    name = Column(String(100), unique=True)  # 名称
    url = Column(String(255), unique=True)  # 地址
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Moviecol %r>' % self.name


# 角色
class Role(Model):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)  # 编号
    name = Column(String(100), unique=True)  # 名称
    auths = Column(String(600), unique=True)  # 地址
    addtime = Column(DateTime, index=True, default=datetime.now)    # 创建时间

    def __repr__(self):
        return '<Role %r>' % self.name














"""
    格式：    字段1 = relationship('外部表class对象', secondary = '关联表名', backref='字段2')
    说明：
    字段1：本表通过“字段1”，查询外部表的字段
    外部表Class对象：sqlalchemy映射的表类
    secondary：多对多关系中，生成的三方表。
    backref：反向查询字段名，相当于在外部表添加一个字段，外部表通过这个字段查询本表字段。

    lazy    1. 默认值为select, 他直接会导出所有的结果对象合成一个列表
            2. dynamic，他会生成一个继承与Query的AppenderQuery对象，可以用于继续做过滤操作。
                        当需要对映射的结果集继续筛选的时候，可以在relationship指定lazy参数为'dynamic'
                    3. 其他的还有很多参数，例如joined，连接查询，但是涉及到查询性能
"""