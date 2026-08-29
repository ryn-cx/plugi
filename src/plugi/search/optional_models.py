from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class VideoPreview(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    uuid: UUID | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300014191(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100060161(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Trailer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    url: str | None = None
    duration: int | None = None

class Field522066(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300012908(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images3 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000645(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images3 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100026239(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images3 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field02284(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images3 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300014190(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images7 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Descriptor(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    description: str | None = None

class Rating8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Images8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300004799(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating8] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Field02283(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300014065(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006778(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100012076(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019067(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300017721(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300005619(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field589618(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019090(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000634(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100008189(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images8 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100054199(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating9] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images20 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field03455(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating21] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images20 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field624896(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images22 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000646(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images22 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100026426(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images22 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field684388(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images22 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field307561(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images22 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field638334(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images27 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100046456(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images28 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019069(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images28 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field589380(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images28 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100010366(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images28 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100021025(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating22] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images32 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field03723(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating33] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images32 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300019210(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300010794(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field03364(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000640(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field568652(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300005821(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300004850(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019837(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field708164(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300010955(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000638(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating34] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating45(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field0300019074(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating45] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating46(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Field0300017793(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images34 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images47(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field307850(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images47 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images48(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300008495(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300018250(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000641(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field530623(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006854(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field520091(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300002072(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019082(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000648(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field465427(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300000610(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images48 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images59(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field313748(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images59 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images60(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100059946(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images60 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019078(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images60 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field274712(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images60 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019076(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images60 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images64(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300021614(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating46] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images64 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating65(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field02067(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating65] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images64 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating66(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images66(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300019449(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating66] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images66 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating67(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field0300000604(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating67] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images66 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating68(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images68(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300007148(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images68 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images69(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300019095(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000644(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300004792(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021652(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300013071(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000637(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019071(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000643(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images69 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images77(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100060110(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images77 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field313749(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images77 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field496979(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images77 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images80(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field01965(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images80 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100040651(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images80 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images82(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field680362(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images82 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images83(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100000647(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images83 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006629(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images83 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300020297(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images83 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000642(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images83 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000635(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images83 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images88(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100029919(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images88 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field512591(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images88 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300014189(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images88 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field590932(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images88 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field04718(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images88 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images93(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300019077(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images93 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300019075(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images93 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000639(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images93 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images96(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100047631(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images96 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field609723(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating68] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images96 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating98(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Images98(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300019408(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating98] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images98 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating99(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Field537347(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images98 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300021618(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images100 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100000636(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images101 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021419(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images101 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field497116(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images101 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images104(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field559079(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images104 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class EpgFeed(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    callsign: str | None = None
    feed_type: str | None = None

class Manifest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class VideoResource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    language: str | None = None

class Schedule(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_time: AwareDatetime | None = None
    live: bool | None = None
    end_time: AwareDatetime | None = None
    program_id: str | None = None

class Images105(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field400000063(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images105 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551234(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images105 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field725756(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images105 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006061(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images105 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field357881(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images105 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images110(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field580545(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images110 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images111(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300016936(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images111 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images112(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field01075(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images112 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images113(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field600005(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images113 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field626743(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images113 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images115(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100013604(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images115 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images116(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field673877(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images116 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100031065(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images116 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images118(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100053843(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating99] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images118 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating119(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field0300001390(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating119] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images118 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Rating120(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Field100003384(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images118 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images121(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field541584(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images121 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field441466(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images121 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images123(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300020964(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images123 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field04558(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images123 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images125(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100042985(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images125 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images126(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field465664(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images126 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field662394(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images126 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field697540(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images126 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images129(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100000893(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images129 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field713869(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images129 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field710259(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images129 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images132(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field590936(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating120] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images132 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating133(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Descriptor] | None = None

class Field0300018951(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating133] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images132 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Rating134(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class Images134(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300011047(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images134 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field599629(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images134 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021011(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images134 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images137(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100014460(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images137 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images138(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field536458(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images138 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images139(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field522098(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images139 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images140(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100050998(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images140 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field484792(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images140 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images142(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field674605(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images142 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images143(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100008293(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images143 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images144(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field456845(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images144 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class VideoResource1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Images145(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field400000059(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource1] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images145 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100004664(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images145 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field688915(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images145 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field497642(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images145 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field667134(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images145 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images150(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field646635(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images150 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images151(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100044464(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images151 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images152(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300021761(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images152 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field456404(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images152 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images154(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field639644(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images154 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100041606(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images154 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300013877(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images154 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field715273(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images154 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images158(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field03714(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images158 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field01622(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images158 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class VideoResource2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Images160(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field724209(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource2] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images160 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images161(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field705476(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images161 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images162(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100029709(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images162 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300016373(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images162 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images164(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300005101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images164 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images165(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field464159(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images165 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field469276(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images165 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100058704(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images165 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images168(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field348095(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images168 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100003132(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images168 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field532498(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images168 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images171(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100060230(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field314504(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field581265(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100015557(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100042096(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field515192(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100014057(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images171 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images178(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field654632(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images178 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images179(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100013642(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images179 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100026989(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images179 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551232(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images179 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field517459(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images179 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field367794(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images179 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images184(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300017682(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images184 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class VideoResource3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Images185(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field711410(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource3] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images185 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field607950(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images185 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field01630(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images185 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100031408(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images185 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images189(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100002884(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images189 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field637768(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images189 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field307852(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images189 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images192(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100010495(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images192 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100043292(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images192 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100013605(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images192 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551211(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images192 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field625147(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images192 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images197(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field626678(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images197 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images198(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field02193(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images198 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images199(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100026163(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images199 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images200(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100056524(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images200 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images201(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100061674(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images201 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images202(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100052322(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images202 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field367686(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images202 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field591336(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images202 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images205(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field516885(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images205 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images206(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100022552(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images206 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006498(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images206 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021914(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images206 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300013924(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images206 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field372439(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images206 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images211(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100002883(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images211 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images212(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300014000(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images212 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field663469(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images212 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field415648(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images212 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images215(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field645252(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images215 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images216(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field610943(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images216 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100031673(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images216 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100027986(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images216 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field579182(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images216 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images220(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field597242(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images220 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images221(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300017139(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images221 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300015509(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images221 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100061356(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images221 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551229(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images221 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images225(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field708086(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images225 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images226(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field602431(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images226 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100055498(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images226 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images228(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field587698(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images228 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100060818(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images228 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300001833(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images228 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field621977(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images228 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images232(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field646601(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100030213(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field329427(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field410747(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field469712(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field594597(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images232 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images238(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100000184(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images238 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field02914(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images238 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006608(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images238 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100000935(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images238 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field710385(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images238 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images243(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100055397(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images243 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images244(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300020390(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images244 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images245(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100007129(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images245 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images246(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100060094(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images246 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100021024(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images246 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021495(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images246 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images249(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100056127(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images249 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images250(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field625477(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images250 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images251(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field303079(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images251 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100043297(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images251 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300017944(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images251 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images254(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field278532(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images254 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images255(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field312629(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images255 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100045807(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images255 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300020923(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images255 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images258(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100039938(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images258 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images259(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field02192(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images259 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field567345(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images259 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100057491(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images259 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field404573(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images259 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images263(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field567311(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images263 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100061793(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images263 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field461204(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images263 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images266(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100015524(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images266 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images267(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field352450(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images267 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006728(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images267 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field634469(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images267 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images270(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field702498(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images270 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images271(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field473448(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images271 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images272(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100000588(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images272 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field709075(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images272 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images274(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field533892(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images274 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images275(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field713868(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images275 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field594102(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images275 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300001752(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images275 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100042340(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images275 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class VideoResource4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Field613761(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource4] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images275 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images280(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100014266(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images280 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300022120(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images280 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field651100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images280 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images283(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field04638(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images283 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100055253(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images283 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field367684(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images283 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images286(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0931(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images286 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field658086(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images286 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images288(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100060992(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100004473(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field574326(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field578316(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100055396(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field571846(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images288 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images294(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field01628(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images294 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images295(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100026825(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images295 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images296(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field537095(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images296 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images297(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field312200(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images297 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images298(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100002689(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images298 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images299(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100055399(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images299 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images300(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300021868(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images300 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images301(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field551295(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images301 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images302(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100060087(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images302 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100061634(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images302 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images304(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100061662(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images304 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021298(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images304 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images306(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field283884(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images306 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images307(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100000702(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field488330(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100004663(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field7954(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field542244(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100019515(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field497327(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images307 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images314(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field543723(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images314 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images315(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field367683(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images315 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images316(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field04294(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images316 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images317(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field642932(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images317 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images318(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field367685(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images318 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images319(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300021952(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300009154(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100018504(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field499567(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field610954(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006856(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images319 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images325(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field568691(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images325 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field312933(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images325 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images327(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field570192(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images327 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100011760(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images327 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field545087(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images327 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field646773(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images327 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images331(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field463724(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images331 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images332(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100011465(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images332 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images333(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field489048(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images333 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images334(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field475643(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images334 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field289796(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images334 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images336(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field656811(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images336 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images337(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100003678(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images337 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images338(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field708292(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images338 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field520251(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images338 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images340(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300008169(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images340 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field278533(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images340 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100055398(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images340 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field528787(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images340 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images344(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field461216(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images344 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images345(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100013527(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100043010(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100038995(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100010530(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100014462(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100058177(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100050578(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field660063(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images345 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images353(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field694144(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images353 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images354(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field575286(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images354 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300017688(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images354 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images356(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300019824(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images356 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images357(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field709637(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images357 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300009147(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images357 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100028012(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images357 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field703989(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images357 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images361(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field678775(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images361 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images362(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field551235(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images362 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100015110(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images362 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100003659(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images362 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100013522(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images362 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Images366(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300006607(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images366 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images367(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field692600(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images367 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class VideoResource5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    ssai_version: str | None = None

class Field400000299(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: EpgFeed | None = None
    video_renditions: list[Any] | None = None
    video_resources: list[VideoResource5] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    subtitles: list[Subtitle] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    schedules: list[Schedule] | None = None
    tags: list[str] | None = None
    images: Images367 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images369(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100057546(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images369 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images370(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field0300016553(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images370 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100057751(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images370 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field641862(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images370 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100044686(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images370 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images374(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field610689(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images374 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images375(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field530171(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images375 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images376(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field552210(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images376 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images377(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100030646(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images377 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field698895(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images377 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100055412(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images377 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300010267(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images377 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021897(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images377 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images382(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300013803(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images382 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images383(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field575310(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images383 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field581281(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images383 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images385(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field100026654(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images385 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images386(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100054211(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images386 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images387(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field0300001104(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images387 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images388(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100003590(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images388 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100058204(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images388 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300021944(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images388 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images391(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field02348(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images391 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field557050(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images391 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images393(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field521033(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images393 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100038731(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images393 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300010397(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[Any] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images393 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images396(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field472705(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images396 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images397(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field688914(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images397 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field466293(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images397 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field04631(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images397 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images400(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field615597(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images400 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300006624(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images400 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[Any] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field100019823(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images400 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images403(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[Any] | None = None

class Field100056268(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field522136(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551215(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field0300004774(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: Any | None = None
    login_reason: str | None = None
    publisher_id: str | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    channel_id: str | None = None
    channel_name: str | None = None
    availability_starts: Any | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    is_recurring: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: Any | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    channel_logo: str | None = None
    player_type: str | None = None
    title: str | None = None

class Field100038732(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field551228(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: Any | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images403 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Images409(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | None = None
    hero_16x9: list[str] | None = None
    hero_422: list[str] | None = None
    hero_feature: list[str] | None = None
    hero_feature_desktop_tablet: list[str] | None = None
    hero_feature_large_mobile: list[str] | None = None
    hero_feature_small_mobile: list[str] | None = None
    landscape_images: list[str] | None = None
    linear_larger_poster: list[str] | None = None
    posterarts: list[str] | None = None
    title_art: list[str] | None = None

class Field577086(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[Any] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images409 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Field464315(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_ends: AwareDatetime | None = None
    year: int | None = None
    epg_feed: Any | None = None
    video_renditions: list[Any] | None = None
    actors: list[str] | None = None
    type: str | None = None
    video_preview_url: str | None = None
    duration: int | None = None
    thumbnails: list[str] | None = None
    needs_login: bool | None = None
    video_previews: list[VideoPreview] | None = None
    availability_duration: int | None = None
    login_reason: str | None = None
    publisher_id: UUID | None = None
    import_id: str | None = None
    description: str | None = None
    id: str | None = None
    ratings: list[Rating134] | None = None
    is_cdc: bool | None = None
    ad_languages: list[str] | None = None
    is_replay: bool | None = None
    availability_starts: AwareDatetime | None = None
    tags: list[str] | None = None
    images: Images409 | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    has_trailer: bool | None = None
    posterarts: list[str] | None = None
    trailers: list[Trailer] | None = None
    content_orientation: str | None = None
    gn_fields: Any | None = None
    backgrounds: list[str] | None = None
    video_metadata: list[Any] | None = None
    directors: list[str] | None = None
    lang: str | None = None
    landscape_images: list[str] | None = None
    player_type: str | None = None
    title: str | None = None

class Contents(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_0300014191: Field0300014191 | None = Field(None, alias='0300014191')
    field_100060161: Field100060161 | None = Field(None, alias='100060161')
    field_522066: Field522066 | None = Field(None, alias='522066')
    field_0300012908: Field0300012908 | None = Field(None, alias='0300012908')
    field_100000645: Field100000645 | None = Field(None, alias='100000645')
    field_100026239: Field100026239 | None = Field(None, alias='100026239')
    field_02284: Field02284 | None = Field(None, alias='02284')
    field_0300014190: Field0300014190 | None = Field(None, alias='0300014190')
    field_0300004799: Field0300004799 | None = Field(None, alias='0300004799')
    field_02283: Field02283 | None = Field(None, alias='02283')
    field_0300014065: Field0300014065 | None = Field(None, alias='0300014065')
    field_0300006778: Field0300006778 | None = Field(None, alias='0300006778')
    field_100012076: Field100012076 | None = Field(None, alias='100012076')
    field_0300019067: Field0300019067 | None = Field(None, alias='0300019067')
    field_0300017721: Field0300017721 | None = Field(None, alias='0300017721')
    field_0300005619: Field0300005619 | None = Field(None, alias='0300005619')
    field_589618: Field589618 | None = Field(None, alias='589618')
    field_0300019090: Field0300019090 | None = Field(None, alias='0300019090')
    field_100000634: Field100000634 | None = Field(None, alias='100000634')
    field_100008189: Field100008189 | None = Field(None, alias='100008189')
    field_100054199: Field100054199 | None = Field(None, alias='100054199')
    field_03455: Field03455 | None = Field(None, alias='03455')
    field_624896: Field624896 | None = Field(None, alias='624896')
    field_100000646: Field100000646 | None = Field(None, alias='100000646')
    field_100026426: Field100026426 | None = Field(None, alias='100026426')
    field_684388: Field684388 | None = Field(None, alias='684388')
    field_307561: Field307561 | None = Field(None, alias='307561')
    field_638334: Field638334 | None = Field(None, alias='638334')
    field_100046456: Field100046456 | None = Field(None, alias='100046456')
    field_0300019069: Field0300019069 | None = Field(None, alias='0300019069')
    field_589380: Field589380 | None = Field(None, alias='589380')
    field_100010366: Field100010366 | None = Field(None, alias='100010366')
    field_100021025: Field100021025 | None = Field(None, alias='100021025')
    field_03723: Field03723 | None = Field(None, alias='03723')
    field_0300019210: Field0300019210 | None = Field(None, alias='0300019210')
    field_0300010794: Field0300010794 | None = Field(None, alias='0300010794')
    field_03364: Field03364 | None = Field(None, alias='03364')
    field_100000640: Field100000640 | None = Field(None, alias='100000640')
    field_568652: Field568652 | None = Field(None, alias='568652')
    field_0300005821: Field0300005821 | None = Field(None, alias='0300005821')
    field_0300004850: Field0300004850 | None = Field(None, alias='0300004850')
    field_0300019837: Field0300019837 | None = Field(None, alias='0300019837')
    field_708164: Field708164 | None = Field(None, alias='708164')
    field_0300010955: Field0300010955 | None = Field(None, alias='0300010955')
    field_100000638: Field100000638 | None = Field(None, alias='100000638')
    field_0300019074: Field0300019074 | None = Field(None, alias='0300019074')
    field_0300017793: Field0300017793 | None = Field(None, alias='0300017793')
    field_307850: Field307850 | None = Field(None, alias='307850')
    field_0300008495: Field0300008495 | None = Field(None, alias='0300008495')
    field_0300018250: Field0300018250 | None = Field(None, alias='0300018250')
    field_100000641: Field100000641 | None = Field(None, alias='100000641')
    field_530623: Field530623 | None = Field(None, alias='530623')
    field_0300006854: Field0300006854 | None = Field(None, alias='0300006854')
    field_520091: Field520091 | None = Field(None, alias='520091')
    field_0300002072: Field0300002072 | None = Field(None, alias='0300002072')
    field_0300019082: Field0300019082 | None = Field(None, alias='0300019082')
    field_100000648: Field100000648 | None = Field(None, alias='100000648')
    field_465427: Field465427 | None = Field(None, alias='465427')
    field_0300000610: Field0300000610 | None = Field(None, alias='0300000610')
    field_313748: Field313748 | None = Field(None, alias='313748')
    field_100059946: Field100059946 | None = Field(None, alias='100059946')
    field_0300019078: Field0300019078 | None = Field(None, alias='0300019078')
    field_274712: Field274712 | None = Field(None, alias='274712')
    field_0300019076: Field0300019076 | None = Field(None, alias='0300019076')
    field_0300021614: Field0300021614 | None = Field(None, alias='0300021614')
    field_02067: Field02067 | None = Field(None, alias='02067')
    field_0300019449: Field0300019449 | None = Field(None, alias='0300019449')
    field_0300000604: Field0300000604 | None = Field(None, alias='0300000604')
    field_0300007148: Field0300007148 | None = Field(None, alias='0300007148')
    field_0300019095: Field0300019095 | None = Field(None, alias='0300019095')
    field_100000644: Field100000644 | None = Field(None, alias='100000644')
    field_0300004792: Field0300004792 | None = Field(None, alias='0300004792')
    field_0300021652: Field0300021652 | None = Field(None, alias='0300021652')
    field_0300013071: Field0300013071 | None = Field(None, alias='0300013071')
    field_100000637: Field100000637 | None = Field(None, alias='100000637')
    field_0300019071: Field0300019071 | None = Field(None, alias='0300019071')
    field_100000643: Field100000643 | None = Field(None, alias='100000643')
    field_100060110: Field100060110 | None = Field(None, alias='100060110')
    field_313749: Field313749 | None = Field(None, alias='313749')
    field_496979: Field496979 | None = Field(None, alias='496979')
    field_01965: Field01965 | None = Field(None, alias='01965')
    field_100040651: Field100040651 | None = Field(None, alias='100040651')
    field_680362: Field680362 | None = Field(None, alias='680362')
    field_100000647: Field100000647 | None = Field(None, alias='100000647')
    field_0300006629: Field0300006629 | None = Field(None, alias='0300006629')
    field_0300020297: Field0300020297 | None = Field(None, alias='0300020297')
    field_100000642: Field100000642 | None = Field(None, alias='100000642')
    field_100000635: Field100000635 | None = Field(None, alias='100000635')
    field_100029919: Field100029919 | None = Field(None, alias='100029919')
    field_512591: Field512591 | None = Field(None, alias='512591')
    field_0300014189: Field0300014189 | None = Field(None, alias='0300014189')
    field_590932: Field590932 | None = Field(None, alias='590932')
    field_04718: Field04718 | None = Field(None, alias='04718')
    field_0300019077: Field0300019077 | None = Field(None, alias='0300019077')
    field_0300019075: Field0300019075 | None = Field(None, alias='0300019075')
    field_100000639: Field100000639 | None = Field(None, alias='100000639')
    field_100047631: Field100047631 | None = Field(None, alias='100047631')
    field_609723: Field609723 | None = Field(None, alias='609723')
    field_0300019408: Field0300019408 | None = Field(None, alias='0300019408')
    field_537347: Field537347 | None = Field(None, alias='537347')
    field_0300021618: Field0300021618 | None = Field(None, alias='0300021618')
    field_100000636: Field100000636 | None = Field(None, alias='100000636')
    field_0300021419: Field0300021419 | None = Field(None, alias='0300021419')
    field_497116: Field497116 | None = Field(None, alias='497116')
    field_559079: Field559079 | None = Field(None, alias='559079')
    field_400000063: Field400000063 | None = Field(None, alias='400000063')
    field_551234: Field551234 | None = Field(None, alias='551234')
    field_725756: Field725756 | None = Field(None, alias='725756')
    field_0300006061: Field0300006061 | None = Field(None, alias='0300006061')
    field_357881: Field357881 | None = Field(None, alias='357881')
    field_580545: Field580545 | None = Field(None, alias='580545')
    field_0300016936: Field0300016936 | None = Field(None, alias='0300016936')
    field_01075: Field01075 | None = Field(None, alias='01075')
    field_600005: Field600005 | None = Field(None, alias='600005')
    field_626743: Field626743 | None = Field(None, alias='626743')
    field_100013604: Field100013604 | None = Field(None, alias='100013604')
    field_673877: Field673877 | None = Field(None, alias='673877')
    field_100031065: Field100031065 | None = Field(None, alias='100031065')
    field_100053843: Field100053843 | None = Field(None, alias='100053843')
    field_0300001390: Field0300001390 | None = Field(None, alias='0300001390')
    field_100003384: Field100003384 | None = Field(None, alias='100003384')
    field_541584: Field541584 | None = Field(None, alias='541584')
    field_441466: Field441466 | None = Field(None, alias='441466')
    field_0300020964: Field0300020964 | None = Field(None, alias='0300020964')
    field_04558: Field04558 | None = Field(None, alias='04558')
    field_100042985: Field100042985 | None = Field(None, alias='100042985')
    field_465664: Field465664 | None = Field(None, alias='465664')
    field_662394: Field662394 | None = Field(None, alias='662394')
    field_697540: Field697540 | None = Field(None, alias='697540')
    field_100000893: Field100000893 | None = Field(None, alias='100000893')
    field_713869: Field713869 | None = Field(None, alias='713869')
    field_710259: Field710259 | None = Field(None, alias='710259')
    field_590936: Field590936 | None = Field(None, alias='590936')
    field_0300018951: Field0300018951 | None = Field(None, alias='0300018951')
    field_0300011047: Field0300011047 | None = Field(None, alias='0300011047')
    field_599629: Field599629 | None = Field(None, alias='599629')
    field_0300021011: Field0300021011 | None = Field(None, alias='0300021011')
    field_100014460: Field100014460 | None = Field(None, alias='100014460')
    field_536458: Field536458 | None = Field(None, alias='536458')
    field_522098: Field522098 | None = Field(None, alias='522098')
    field_100050998: Field100050998 | None = Field(None, alias='100050998')
    field_484792: Field484792 | None = Field(None, alias='484792')
    field_674605: Field674605 | None = Field(None, alias='674605')
    field_100008293: Field100008293 | None = Field(None, alias='100008293')
    field_456845: Field456845 | None = Field(None, alias='456845')
    field_400000059: Field400000059 | None = Field(None, alias='400000059')
    field_100004664: Field100004664 | None = Field(None, alias='100004664')
    field_688915: Field688915 | None = Field(None, alias='688915')
    field_497642: Field497642 | None = Field(None, alias='497642')
    field_667134: Field667134 | None = Field(None, alias='667134')
    field_646635: Field646635 | None = Field(None, alias='646635')
    field_100044464: Field100044464 | None = Field(None, alias='100044464')
    field_0300021761: Field0300021761 | None = Field(None, alias='0300021761')
    field_456404: Field456404 | None = Field(None, alias='456404')
    field_639644: Field639644 | None = Field(None, alias='639644')
    field_100041606: Field100041606 | None = Field(None, alias='100041606')
    field_0300013877: Field0300013877 | None = Field(None, alias='0300013877')
    field_715273: Field715273 | None = Field(None, alias='715273')
    field_03714: Field03714 | None = Field(None, alias='03714')
    field_01622: Field01622 | None = Field(None, alias='01622')
    field_724209: Field724209 | None = Field(None, alias='724209')
    field_705476: Field705476 | None = Field(None, alias='705476')
    field_100029709: Field100029709 | None = Field(None, alias='100029709')
    field_0300016373: Field0300016373 | None = Field(None, alias='0300016373')
    field_0300005101: Field0300005101 | None = Field(None, alias='0300005101')
    field_464159: Field464159 | None = Field(None, alias='464159')
    field_469276: Field469276 | None = Field(None, alias='469276')
    field_100058704: Field100058704 | None = Field(None, alias='100058704')
    field_348095: Field348095 | None = Field(None, alias='348095')
    field_100003132: Field100003132 | None = Field(None, alias='100003132')
    field_532498: Field532498 | None = Field(None, alias='532498')
    field_100060230: Field100060230 | None = Field(None, alias='100060230')
    field_314504: Field314504 | None = Field(None, alias='314504')
    field_581265: Field581265 | None = Field(None, alias='581265')
    field_100015557: Field100015557 | None = Field(None, alias='100015557')
    field_100042096: Field100042096 | None = Field(None, alias='100042096')
    field_515192: Field515192 | None = Field(None, alias='515192')
    field_100014057: Field100014057 | None = Field(None, alias='100014057')
    field_654632: Field654632 | None = Field(None, alias='654632')
    field_100013642: Field100013642 | None = Field(None, alias='100013642')
    field_100026989: Field100026989 | None = Field(None, alias='100026989')
    field_551232: Field551232 | None = Field(None, alias='551232')
    field_517459: Field517459 | None = Field(None, alias='517459')
    field_367794: Field367794 | None = Field(None, alias='367794')
    field_0300017682: Field0300017682 | None = Field(None, alias='0300017682')
    field_711410: Field711410 | None = Field(None, alias='711410')
    field_607950: Field607950 | None = Field(None, alias='607950')
    field_01630: Field01630 | None = Field(None, alias='01630')
    field_100031408: Field100031408 | None = Field(None, alias='100031408')
    field_100002884: Field100002884 | None = Field(None, alias='100002884')
    field_637768: Field637768 | None = Field(None, alias='637768')
    field_307852: Field307852 | None = Field(None, alias='307852')
    field_100010495: Field100010495 | None = Field(None, alias='100010495')
    field_100043292: Field100043292 | None = Field(None, alias='100043292')
    field_100013605: Field100013605 | None = Field(None, alias='100013605')
    field_551211: Field551211 | None = Field(None, alias='551211')
    field_625147: Field625147 | None = Field(None, alias='625147')
    field_626678: Field626678 | None = Field(None, alias='626678')
    field_02193: Field02193 | None = Field(None, alias='02193')
    field_100026163: Field100026163 | None = Field(None, alias='100026163')
    field_100056524: Field100056524 | None = Field(None, alias='100056524')
    field_100061674: Field100061674 | None = Field(None, alias='100061674')
    field_100052322: Field100052322 | None = Field(None, alias='100052322')
    field_367686: Field367686 | None = Field(None, alias='367686')
    field_591336: Field591336 | None = Field(None, alias='591336')
    field_516885: Field516885 | None = Field(None, alias='516885')
    field_100022552: Field100022552 | None = Field(None, alias='100022552')
    field_0300006498: Field0300006498 | None = Field(None, alias='0300006498')
    field_0300021914: Field0300021914 | None = Field(None, alias='0300021914')
    field_0300013924: Field0300013924 | None = Field(None, alias='0300013924')
    field_372439: Field372439 | None = Field(None, alias='372439')
    field_100002883: Field100002883 | None = Field(None, alias='100002883')
    field_0300014000: Field0300014000 | None = Field(None, alias='0300014000')
    field_663469: Field663469 | None = Field(None, alias='663469')
    field_415648: Field415648 | None = Field(None, alias='415648')
    field_645252: Field645252 | None = Field(None, alias='645252')
    field_610943: Field610943 | None = Field(None, alias='610943')
    field_100031673: Field100031673 | None = Field(None, alias='100031673')
    field_100027986: Field100027986 | None = Field(None, alias='100027986')
    field_579182: Field579182 | None = Field(None, alias='579182')
    field_597242: Field597242 | None = Field(None, alias='597242')
    field_0300017139: Field0300017139 | None = Field(None, alias='0300017139')
    field_0300015509: Field0300015509 | None = Field(None, alias='0300015509')
    field_100061356: Field100061356 | None = Field(None, alias='100061356')
    field_551229: Field551229 | None = Field(None, alias='551229')
    field_708086: Field708086 | None = Field(None, alias='708086')
    field_602431: Field602431 | None = Field(None, alias='602431')
    field_100055498: Field100055498 | None = Field(None, alias='100055498')
    field_587698: Field587698 | None = Field(None, alias='587698')
    field_100060818: Field100060818 | None = Field(None, alias='100060818')
    field_0300001833: Field0300001833 | None = Field(None, alias='0300001833')
    field_621977: Field621977 | None = Field(None, alias='621977')
    field_646601: Field646601 | None = Field(None, alias='646601')
    field_100030213: Field100030213 | None = Field(None, alias='100030213')
    field_329427: Field329427 | None = Field(None, alias='329427')
    field_410747: Field410747 | None = Field(None, alias='410747')
    field_469712: Field469712 | None = Field(None, alias='469712')
    field_594597: Field594597 | None = Field(None, alias='594597')
    field_100000184: Field100000184 | None = Field(None, alias='100000184')
    field_02914: Field02914 | None = Field(None, alias='02914')
    field_0300006608: Field0300006608 | None = Field(None, alias='0300006608')
    field_100000935: Field100000935 | None = Field(None, alias='100000935')
    field_710385: Field710385 | None = Field(None, alias='710385')
    field_100055397: Field100055397 | None = Field(None, alias='100055397')
    field_0300020390: Field0300020390 | None = Field(None, alias='0300020390')
    field_100007129: Field100007129 | None = Field(None, alias='100007129')
    field_100060094: Field100060094 | None = Field(None, alias='100060094')
    field_100021024: Field100021024 | None = Field(None, alias='100021024')
    field_0300021495: Field0300021495 | None = Field(None, alias='0300021495')
    field_100056127: Field100056127 | None = Field(None, alias='100056127')
    field_625477: Field625477 | None = Field(None, alias='625477')
    field_303079: Field303079 | None = Field(None, alias='303079')
    field_100043297: Field100043297 | None = Field(None, alias='100043297')
    field_0300017944: Field0300017944 | None = Field(None, alias='0300017944')
    field_278532: Field278532 | None = Field(None, alias='278532')
    field_312629: Field312629 | None = Field(None, alias='312629')
    field_100045807: Field100045807 | None = Field(None, alias='100045807')
    field_0300020923: Field0300020923 | None = Field(None, alias='0300020923')
    field_100039938: Field100039938 | None = Field(None, alias='100039938')
    field_02192: Field02192 | None = Field(None, alias='02192')
    field_567345: Field567345 | None = Field(None, alias='567345')
    field_100057491: Field100057491 | None = Field(None, alias='100057491')
    field_404573: Field404573 | None = Field(None, alias='404573')
    field_567311: Field567311 | None = Field(None, alias='567311')
    field_100061793: Field100061793 | None = Field(None, alias='100061793')
    field_461204: Field461204 | None = Field(None, alias='461204')
    field_100015524: Field100015524 | None = Field(None, alias='100015524')
    field_352450: Field352450 | None = Field(None, alias='352450')
    field_0300006728: Field0300006728 | None = Field(None, alias='0300006728')
    field_634469: Field634469 | None = Field(None, alias='634469')
    field_702498: Field702498 | None = Field(None, alias='702498')
    field_473448: Field473448 | None = Field(None, alias='473448')
    field_100000588: Field100000588 | None = Field(None, alias='100000588')
    field_709075: Field709075 | None = Field(None, alias='709075')
    field_533892: Field533892 | None = Field(None, alias='533892')
    field_713868: Field713868 | None = Field(None, alias='713868')
    field_594102: Field594102 | None = Field(None, alias='594102')
    field_0300001752: Field0300001752 | None = Field(None, alias='0300001752')
    field_100042340: Field100042340 | None = Field(None, alias='100042340')
    field_613761: Field613761 | None = Field(None, alias='613761')
    field_100014266: Field100014266 | None = Field(None, alias='100014266')
    field_0300022120: Field0300022120 | None = Field(None, alias='0300022120')
    field_651100: Field651100 | None = Field(None, alias='651100')
    field_04638: Field04638 | None = Field(None, alias='04638')
    field_100055253: Field100055253 | None = Field(None, alias='100055253')
    field_367684: Field367684 | None = Field(None, alias='367684')
    field_0931: Field0931 | None = Field(None, alias='0931')
    field_658086: Field658086 | None = Field(None, alias='658086')
    field_100060992: Field100060992 | None = Field(None, alias='100060992')
    field_100004473: Field100004473 | None = Field(None, alias='100004473')
    field_574326: Field574326 | None = Field(None, alias='574326')
    field_578316: Field578316 | None = Field(None, alias='578316')
    field_100055396: Field100055396 | None = Field(None, alias='100055396')
    field_571846: Field571846 | None = Field(None, alias='571846')
    field_01628: Field01628 | None = Field(None, alias='01628')
    field_100026825: Field100026825 | None = Field(None, alias='100026825')
    field_537095: Field537095 | None = Field(None, alias='537095')
    field_312200: Field312200 | None = Field(None, alias='312200')
    field_100002689: Field100002689 | None = Field(None, alias='100002689')
    field_100055399: Field100055399 | None = Field(None, alias='100055399')
    field_0300021868: Field0300021868 | None = Field(None, alias='0300021868')
    field_551295: Field551295 | None = Field(None, alias='551295')
    field_100060087: Field100060087 | None = Field(None, alias='100060087')
    field_100061634: Field100061634 | None = Field(None, alias='100061634')
    field_100061662: Field100061662 | None = Field(None, alias='100061662')
    field_0300021298: Field0300021298 | None = Field(None, alias='0300021298')
    field_283884: Field283884 | None = Field(None, alias='283884')
    field_100000702: Field100000702 | None = Field(None, alias='100000702')
    field_488330: Field488330 | None = Field(None, alias='488330')
    field_100004663: Field100004663 | None = Field(None, alias='100004663')
    field_7954: Field7954 | None = Field(None, alias='7954')
    field_542244: Field542244 | None = Field(None, alias='542244')
    field_100019515: Field100019515 | None = Field(None, alias='100019515')
    field_497327: Field497327 | None = Field(None, alias='497327')
    field_543723: Field543723 | None = Field(None, alias='543723')
    field_367683: Field367683 | None = Field(None, alias='367683')
    field_04294: Field04294 | None = Field(None, alias='04294')
    field_642932: Field642932 | None = Field(None, alias='642932')
    field_367685: Field367685 | None = Field(None, alias='367685')
    field_0300021952: Field0300021952 | None = Field(None, alias='0300021952')
    field_0300009154: Field0300009154 | None = Field(None, alias='0300009154')
    field_100018504: Field100018504 | None = Field(None, alias='100018504')
    field_499567: Field499567 | None = Field(None, alias='499567')
    field_610954: Field610954 | None = Field(None, alias='610954')
    field_0300006856: Field0300006856 | None = Field(None, alias='0300006856')
    field_568691: Field568691 | None = Field(None, alias='568691')
    field_312933: Field312933 | None = Field(None, alias='312933')
    field_570192: Field570192 | None = Field(None, alias='570192')
    field_100011760: Field100011760 | None = Field(None, alias='100011760')
    field_545087: Field545087 | None = Field(None, alias='545087')
    field_646773: Field646773 | None = Field(None, alias='646773')
    field_463724: Field463724 | None = Field(None, alias='463724')
    field_100011465: Field100011465 | None = Field(None, alias='100011465')
    field_489048: Field489048 | None = Field(None, alias='489048')
    field_475643: Field475643 | None = Field(None, alias='475643')
    field_289796: Field289796 | None = Field(None, alias='289796')
    field_656811: Field656811 | None = Field(None, alias='656811')
    field_100003678: Field100003678 | None = Field(None, alias='100003678')
    field_708292: Field708292 | None = Field(None, alias='708292')
    field_520251: Field520251 | None = Field(None, alias='520251')
    field_0300008169: Field0300008169 | None = Field(None, alias='0300008169')
    field_278533: Field278533 | None = Field(None, alias='278533')
    field_100055398: Field100055398 | None = Field(None, alias='100055398')
    field_528787: Field528787 | None = Field(None, alias='528787')
    field_461216: Field461216 | None = Field(None, alias='461216')
    field_100013527: Field100013527 | None = Field(None, alias='100013527')
    field_100043010: Field100043010 | None = Field(None, alias='100043010')
    field_100038995: Field100038995 | None = Field(None, alias='100038995')
    field_100010530: Field100010530 | None = Field(None, alias='100010530')
    field_100014462: Field100014462 | None = Field(None, alias='100014462')
    field_100058177: Field100058177 | None = Field(None, alias='100058177')
    field_100050578: Field100050578 | None = Field(None, alias='100050578')
    field_660063: Field660063 | None = Field(None, alias='660063')
    field_694144: Field694144 | None = Field(None, alias='694144')
    field_575286: Field575286 | None = Field(None, alias='575286')
    field_0300017688: Field0300017688 | None = Field(None, alias='0300017688')
    field_0300019824: Field0300019824 | None = Field(None, alias='0300019824')
    field_709637: Field709637 | None = Field(None, alias='709637')
    field_0300009147: Field0300009147 | None = Field(None, alias='0300009147')
    field_100028012: Field100028012 | None = Field(None, alias='100028012')
    field_703989: Field703989 | None = Field(None, alias='703989')
    field_678775: Field678775 | None = Field(None, alias='678775')
    field_551235: Field551235 | None = Field(None, alias='551235')
    field_100015110: Field100015110 | None = Field(None, alias='100015110')
    field_100003659: Field100003659 | None = Field(None, alias='100003659')
    field_100013522: Field100013522 | None = Field(None, alias='100013522')
    field_0300006607: Field0300006607 | None = Field(None, alias='0300006607')
    field_692600: Field692600 | None = Field(None, alias='692600')
    field_400000299: Field400000299 | None = Field(None, alias='400000299')
    field_100057546: Field100057546 | None = Field(None, alias='100057546')
    field_0300016553: Field0300016553 | None = Field(None, alias='0300016553')
    field_100057751: Field100057751 | None = Field(None, alias='100057751')
    field_641862: Field641862 | None = Field(None, alias='641862')
    field_100044686: Field100044686 | None = Field(None, alias='100044686')
    field_610689: Field610689 | None = Field(None, alias='610689')
    field_530171: Field530171 | None = Field(None, alias='530171')
    field_552210: Field552210 | None = Field(None, alias='552210')
    field_100030646: Field100030646 | None = Field(None, alias='100030646')
    field_698895: Field698895 | None = Field(None, alias='698895')
    field_100055412: Field100055412 | None = Field(None, alias='100055412')
    field_0300010267: Field0300010267 | None = Field(None, alias='0300010267')
    field_0300021897: Field0300021897 | None = Field(None, alias='0300021897')
    field_0300013803: Field0300013803 | None = Field(None, alias='0300013803')
    field_575310: Field575310 | None = Field(None, alias='575310')
    field_581281: Field581281 | None = Field(None, alias='581281')
    field_100026654: Field100026654 | None = Field(None, alias='100026654')
    field_100054211: Field100054211 | None = Field(None, alias='100054211')
    field_0300001104: Field0300001104 | None = Field(None, alias='0300001104')
    field_100003590: Field100003590 | None = Field(None, alias='100003590')
    field_100058204: Field100058204 | None = Field(None, alias='100058204')
    field_0300021944: Field0300021944 | None = Field(None, alias='0300021944')
    field_02348: Field02348 | None = Field(None, alias='02348')
    field_557050: Field557050 | None = Field(None, alias='557050')
    field_521033: Field521033 | None = Field(None, alias='521033')
    field_100038731: Field100038731 | None = Field(None, alias='100038731')
    field_0300010397: Field0300010397 | None = Field(None, alias='0300010397')
    field_472705: Field472705 | None = Field(None, alias='472705')
    field_688914: Field688914 | None = Field(None, alias='688914')
    field_466293: Field466293 | None = Field(None, alias='466293')
    field_04631: Field04631 | None = Field(None, alias='04631')
    field_615597: Field615597 | None = Field(None, alias='615597')
    field_0300006624: Field0300006624 | None = Field(None, alias='0300006624')
    field_100019823: Field100019823 | None = Field(None, alias='100019823')
    field_100056268: Field100056268 | None = Field(None, alias='100056268')
    field_522136: Field522136 | None = Field(None, alias='522136')
    field_551215: Field551215 | None = Field(None, alias='551215')
    field_0300004774: Field0300004774 | None = Field(None, alias='0300004774')
    field_100038732: Field100038732 | None = Field(None, alias='100038732')
    field_551228: Field551228 | None = Field(None, alias='551228')
    field_577086: Field577086 | None = Field(None, alias='577086')
    field_464315: Field464315 | None = Field(None, alias='464315')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    type: str | None = None

class Container(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None
    id: str | None = None
    items: list[Item] | None = None
    title: str | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    apps: dict[str, Any] | None = None
    contents: Contents | None = None
    valid_duration: int | None = None
    personalization_id: UUID | None = None
    containers: list[Container] | None = None
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
