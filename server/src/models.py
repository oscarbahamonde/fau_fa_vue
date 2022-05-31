from pydantic import BaseModel, HttpUrl, EmailStr, Field, validator
from sqlmodel import SQLModel
from typing import Optional, List, Dict, Union
from datetime import datetime, date, time
from uuid import UUID, uuid4
from boto3.dynamodb.types import Binary
from decimal import Decimal
from enum import Enum

class reactions(str, Enum):
    like = '👍'
    dislike = '👎'
    love = '❤️'
    laugh = '😂'
    sad = '😢'
    angry = '😡'
    thinking = '🤔'
    confused = '😕'

class roles(str, Enum):
    admin = 'admin'
    user = 'user'
    account = 'account'

class users(BaseModel):
    id: str
    username: str
    email: EmailStr
    picture: Optional[HttpUrl]
    role: roles = Field(default=roles.user)

class time_info(BaseModel):
    time: str = Field(default=datetime.now().strftime('%H:%M:%S'))
    date: str = Field(default=datetime.now().strftime('%Y-%m-%d'))
    timestamp:float = datetime.now().timestamp()
    @property
    def relative_time(ts:float)->str:
        if (datetime.now().timestamp() - ts) < 60:
            return 'Less than a minute ago'
        elif (datetime.now().timestamp() - ts) < 3600:
            return f'{int((datetime.now().timestamp() - ts)/60)} minutes ago'
        elif (datetime.now().timestamp() - ts) < 86400:
            return f'{int((datetime.now().timestamp() - ts)/3600)} hours ago'
        elif (datetime.now().timestamp() - ts) < 604800:
            return f'{int((datetime.now().timestamp() - ts)/86400)} days ago'
        elif (datetime.now().timestamp() - ts) < 2419200:
            return f'{int((datetime.now().timestamp() - ts)/604800)} weeks ago'
        else:
            return f'{int((datetime.now().timestamp() - ts)/2419200)} months ago'

class reaction(BaseModel):
    uid: str
    reaction: reactions
    time_stamp: time_info = time_info()
    @validator('reaction', pre=True, always=True)
    def one_reaction_per_user(cls, v):
        if v.user.id in reaction.user.id:
            raise ValueError('You can only react once')

class media(BaseModel):
    id: str = Field(...)
    uid: str = Field(...)
    file: Optional[str] = Field()
    filename: str = Field(...)
    url: HttpUrl = Field(...)
    size: Optional[str] = Field()
    content_type: Optional[str] = Field()
    last_modified: Optional[str] = Field()
    extension: Optional[str] = Field()

class comments(BaseModel):
    id: str = Field(...)
    uid: str = Field(...)
    comment: str = Field(...)
    time: time_info = Field(...)
    reactions: List[Optional[reaction]] = Field()
    media: List[Optional[media]] 
    @property
    def reactions_count_sorted(self)->List[reaction]:
        reactions_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in reactions_sorted:
                reactions_sorted[reaction.reaction] += 1
            else:
                reactions_sorted[reaction.reaction] = 1

class posts(BaseModel):
    id: str = Field(...)
    uid: str = Field(...)
    title: str = Field(...)
    description: Optional[str] = Field()
    content: str = Field(...)
    media: List[Optional[media]] 
    comments: List[Optional[comments]] 
    reactions: List[Optional[reaction]] 
    time_stamp: time_info = time_info()
    @property
    def reactions_count_sorted(self)->List[reaction]:
        reactions_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in reactions_sorted:
                reactions_sorted[reaction.reaction] += 1
            else:
                reactions_sorted[reaction.reaction] = 1
    @property
    def comments_count_sorted_by_reaction(self)->Dict[reactions, int]:
        comments_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in comments_sorted:
                comments_sorted[reaction.reaction] += 1
            else:
                comments_sorted[reaction.reaction] = 1
        return comments_sorted
    @property
    def comments_count_sorted_by_user(self)->Dict[users, int]:
        comments_sorted = {}
        for comment in self.comments:
            if comment.user.id in comments_sorted:
                comments_sorted[comment.user.id] += 1
            else:
                comments_sorted[comment.user.id] = 1
        return comments_sorted
    
class tracks(media):
    title: str = Field(...)
    artist: str = Field(...)
    album: str = Field(...)
    thumbnail: Optional[HttpUrl] = Field()
    duration: Optional[str] = Field()
    views: Optional[int] = Field(default=0)
    reactions: List[Optional[reaction]] 
    comments: List[Optional[comments]] 
    @property
    def reactions_count_sorted(self)->List[reaction]:
        reactions_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in reactions_sorted:
                reactions_sorted[reaction.reaction] += 1
            else:
                reactions_sorted[reaction.reaction] = 1
        return reactions_sorted
    
class images(media):
    caption: str = Field(...)
    reactions: List[Optional[reaction]]
    comments: List[Optional[comments]] 
    @property
    def reactions_count_sorted(self)->List[reaction]:
        reactions_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in reactions_sorted:
                reactions_sorted[reaction.reaction] += 1
            else:
                reactions_sorted[reaction.reaction] = 1
        return reactions_sorted

class videos(media):
    title: str = Field(...)
    duration: Optional[str] = Field()
    views: Optional[int] = Field(default=0)
    reactions: List[Optional[reaction]] 
    comments: List[Optional[comments]] 
    @property
    def reactions_count_sorted(self)->List[reaction]:
        reactions_sorted = {}
        for reaction in self.reactions:
            if reaction.reaction in reactions_sorted:
                reactions_sorted[reaction.reaction] += 1
            else:
                reactions_sorted[reaction.reaction] = 1
        return reactions_sorted

class Interaction(posts or comments or reactions):
    pass

class Content(tracks or images or videos):
    pass

class skills(BaseModel):
    id: str = Field(...)
    uid: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    icon: Optional[str] = Field()
    level: Optional[int] = Field(min_value=0, max_value=100)

class projects(BaseModel):
    id: str = Field(...)
    uid: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    thumbnail: Optional[HttpUrl] = Field()
    content: List[Optional[Content]] 

class profiles(users):
    title: str = Field(...)
    description: str = Field(...)
    followers: List[Optional[users]] 
    following: List[Optional[users]] 
    wallpaper: Optional[HttpUrl] = Field()
    content: List[Optional[Content]] 
    skills: List[Optional[skills]]
    projects: List[Optional[projects]] 
    interactions: List[Optional[Interaction]]
    