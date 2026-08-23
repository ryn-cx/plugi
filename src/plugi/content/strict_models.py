from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel

class Subtitle(BaseModel):
    url: str
    lang: str
    lang_alpha3: str
    lang_translation: str

class CreditCuepoints(BaseModel):
    postlude: float
    prologue: float
    intro_start: float
    intro_end: float
    recap_start: float
    recap_end: float
    earlycredits_start: float
    earlycredits_end: float
    prelogue: float

class Rating(BaseModel):
    code: str
    system: str
    value: str
    descriptors: list[None]

class AudioTrack(BaseModel):
    type: str
    lang: str
    display_name: str

class Manifest(BaseModel):
    url: str
    duration: int

class VideoResource(BaseModel):
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Monetization(BaseModel):
    cue_points: list[float]

class Awards(BaseModel):
    items: list[None]

class Images(BaseModel):
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

class VideoMetadatum(BaseModel):
    type: str
    codec: str
    resolution: str

class VideoPreview(BaseModel):
    source: str
    url: str
    uuid: UUID

class VideoResource1(BaseModel):
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Child1(BaseModel):
    is_cdc: bool
    directors: list[str]
    url: str
    has_trailer: bool
    air_datetime: None
    series_id: str
    creator_tensor_app: None
    tubi_fields: dict[str, Any]
    detailed_type: str
    canonical_id: str
    description: str
    has_subtitle: bool
    availability_ends: None
    ratings: list[Rating]
    internal_tags: list[None]
    monetization: Monetization
    video_renditions: list[None]
    player_type: str
    type: str
    import_id: str
    imdb_id: None
    video_resources: list[VideoResource1]
    lang: str
    gracenote_id: str
    trailers: list[None]
    country: str
    posterarts: list[str]
    video_metadata: list[None]
    needs_login: bool
    video_previews: list[None]
    content_orientation: str
    partner_id: None
    publisher_id: UUID
    is_replay: bool
    policy_match: bool
    landscape_images: list[str]
    episode_number: str
    availability_duration: int
    hero_images: list[str]
    images: Images
    id: str
    updated_at: AwareDatetime
    credit_cuepoints: CreditCuepoints
    ad_languages: list[None]
    imdb_fields: None
    year: int
    duration: int
    version: int
    backgrounds: list[str]
    actors: list[str]
    rt_fields: None
    login_reason: str
    subtitles: list[None]
    version_id: str
    availability_starts: AwareDatetime
    thumbnails: list[str]
    awards: Awards
    tags: list[str]
    gn_fields: None
    display_episode_number: str
    title: str
    video_preview_url: str

class Child(BaseModel):
    id: str
    type: str
    title: str
    children: list[Child1]
    posterarts: list[None]

class ContentModel(BaseModel):
    imdb_fields: None
    channel_logo: str | None = None
    landscape_images: list[str]
    url: str | None = None
    subtitles: list[Subtitle]
    gn_fields: None
    gracenote_id: str | None
    is_cdc: bool
    tubi_fields: dict[str, Any]
    player_type: str
    credit_cuepoints: CreditCuepoints | None = None
    lang: str
    has_trailer: bool
    description: str
    valid_duration: int
    ratings: list[Rating]
    detailed_type: str
    channel_id: str | None = None
    is_replay: bool
    channel_name: str | None = None
    thumbnails: list[str]
    partner_id: None
    country: str
    video_resources: list[VideoResource] | None = None
    needs_login: bool
    type: str
    channel_logo_long: str | None = None
    monetization: Monetization | None = None
    version_id: str
    actors: list[str]
    internal_tags: list[None]
    video_renditions: list[None]
    availability_duration: int | None
    publisher_id: UUID | str = Field(union_mode='left_to_right')
    canonical_id: str
    air_datetime: None
    channel_logo_short: str | None = None
    posterarts: list[str]
    trailers: list[None]
    availability_ends: None
    policy_match: bool
    login_reason: str
    directors: list[str]
    rt_fields: None
    updated_at: AwareDatetime
    id: str
    channel_logo_center: str | None = None
    awards: Awards
    title: str
    import_id: str
    ad_languages: list[None]
    duration: int | None = None
    version: int
    video_preview_url: str
    content_orientation: str
    availability_starts: AwareDatetime | None
    images: Images
    hero_images: list[str]
    has_subtitle: bool
    video_metadata: list[VideoMetadatum] | None = None
    tags: list[str]
    imdb_id: str | None
    backgrounds: list[str]
    video_previews: list[VideoPreview]
    creator_tensor_app: None
    year: int
    series_id: str | None = None
    display_episode_number: str | None = None
    episode_number: str | None = None
    is_recurring: bool | None = None
    is_sequential: bool | None = None
    children: list[Child] | None = None
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
