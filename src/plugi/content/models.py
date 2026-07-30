from pydantic import Field
from typing import Any
from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict

class VideoPreview(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    url: str
    uuid: UUID

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str
    system: str
    value: str
    descriptors: list[None]

class CreditCuepoints(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    postlude: float
    prologue: float
    intro_start: float
    intro_end: float
    recap_start: float
    recap_end: float
    earlycredits_start: float
    earlycredits_end: float
    prelogue: float

class AudioTrack(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    lang: str
    display_name: str

class Manifest(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    duration: int

class VideoResource(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Subtitle(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    lang: str
    lang_alpha3: str
    lang_translation: str

class VideoMetadatum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    codec: str
    resolution: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    backgrounds: list[str]
    hero_16x9: list[str]
    hero_422: list[str]
    hero_feature: list[str]
    hero_feature_desktop_tablet: list[str]
    hero_feature_large_mobile: list[str]
    hero_feature_small_mobile: list[str]
    landscape_images: list[str]
    linear_larger_poster: list[str]
    posterarts: list[str]
    title_art: list[None]

class Awards(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    items: list[None]

class Monetization(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    cue_points: list[float]

class VideoResource1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Child1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    trailers: list[None]
    updated_at: AwareDatetime
    video_previews: list[None]
    creator_tensor_app: None
    images: Images
    video_resources: list[VideoResource1]
    availability_ends: None
    description: str
    imdb_id: None
    backgrounds: list[str]
    title: str
    publisher_id: UUID
    imdb_fields: None
    tags: list[str]
    canonical_id: str
    partner_id: None
    has_subtitle: bool
    country: str
    availability_duration: int
    ratings: list[Rating]
    availability_starts: AwareDatetime
    type: str
    tubi_fields: dict[str, Any]
    actors: list[str]
    lang: str
    hero_images: list[str]
    duration: int
    subtitles: list[None]
    is_cdc: bool
    video_preview_url: str
    gracenote_id: str
    landscape_images: list[str]
    ad_languages: list[None]
    series_id: str
    year: int
    air_datetime: None
    display_episode_number: str
    login_reason: str
    policy_match: bool
    content_orientation: str
    video_renditions: list[None]
    thumbnails: list[str]
    video_metadata: list[None]
    episode_number: str
    id: str
    directors: list[str]
    version: int
    detailed_type: str
    has_trailer: bool
    credit_cuepoints: CreditCuepoints
    rt_fields: None
    url: str
    posterarts: list[str]
    player_type: str
    is_replay: bool
    gn_fields: None
    internal_tags: list[None]
    needs_login: bool
    awards: Awards
    version_id: str
    monetization: Monetization
    import_id: str

class Child(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str
    title: str
    children: list[Child1]
    posterarts: list[None]

class ContentModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    publisher_id: UUID | str = Field(union_mode='left_to_right')
    video_previews: list[VideoPreview]
    channel_logo: str | None = None
    duration: int | None = None
    import_id: str
    lang: str
    backgrounds: list[str]
    content_orientation: str
    ratings: list[Rating]
    creator_tensor_app: None
    partner_id: None
    internal_tags: list[None]
    availability_ends: None
    description: str
    credit_cuepoints: CreditCuepoints | None = None
    tags: list[str]
    availability_duration: int | None
    url: str | None = None
    rt_fields: None
    imdb_fields: None
    video_resources: list[VideoResource] | None = None
    availability_starts: AwareDatetime | None
    imdb_id: str | None
    policy_match: bool
    login_reason: str
    hero_images: list[str]
    type: str
    tubi_fields: dict[str, Any]
    subtitles: list[Subtitle]
    video_metadata: list[VideoMetadatum] | None = None
    channel_logo_short: str | None = None
    detailed_type: str
    gn_fields: None
    images: Images
    updated_at: AwareDatetime
    channel_logo_long: str | None = None
    gracenote_id: str | None
    video_preview_url: str
    awards: Awards
    player_type: str
    ad_languages: list[None]
    is_replay: bool
    monetization: Monetization | None = None
    directors: list[str]
    air_datetime: None
    channel_id: str | None = None
    video_renditions: list[None]
    posterarts: list[str]
    valid_duration: int
    id: str
    thumbnails: list[str]
    version_id: str
    version: int
    trailers: list[None]
    has_trailer: bool
    has_subtitle: bool
    title: str
    channel_logo_center: str | None = None
    landscape_images: list[str]
    country: str
    needs_login: bool
    canonical_id: str
    channel_name: str | None = None
    year: int
    actors: list[str]
    is_cdc: bool
    series_id: str | None = None
    display_episode_number: str | None = None
    episode_number: str | None = None
    is_recurring: bool | None = None
    is_sequential: bool | None = None
    children: list[Child] | None = None
