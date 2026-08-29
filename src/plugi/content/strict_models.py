from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import ConfigDict
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel

class Subtitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    lang: str
    lang_alpha3: str
    lang_translation: str

class CreditCuepoints(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    model_config = ConfigDict(defer_build=True)
    code: str
    system: str
    value: str
    descriptors: list[None]

class AudioTrack(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    lang: str
    display_name: str

class Manifest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    duration: int

class VideoResource(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Monetization(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cue_points: list[float]

class Awards(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[None]

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    title_art: list[str]

class VideoMetadatum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    codec: str
    resolution: str

class VideoPreview(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    url: str
    uuid: UUID

class Images1(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class VideoResource1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    codec: str
    audio_tracks: list[AudioTrack]
    resolution: str
    manifest: Manifest
    titan_version: str
    ssai_version: str
    generator_version: str

class Child1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_number: str
    internal_tags: list[None]
    version_id: str
    content_orientation: str
    awards: Awards
    player_type: str
    is_replay: bool
    canonical_id: str
    video_preview_url: str
    description: str
    gn_fields: None
    lang: str
    directors: list[str]
    video_renditions: list[None]
    images: Images1
    import_id: str
    duration: int
    publisher_id: UUID
    needs_login: bool
    ratings: list[Rating]
    availability_starts: AwareDatetime
    series_id: str
    year: int
    has_trailer: bool
    type: str
    tubi_fields: dict[str, Any]
    landscape_images: list[str]
    video_previews: list[None]
    display_episode_number: str
    actors: list[str]
    video_metadata: list[None]
    monetization: Monetization
    country: str
    trailers: list[None]
    video_resources: list[VideoResource1]
    subtitles: list[Subtitle]
    gracenote_id: str
    backgrounds: list[str]
    has_subtitle: bool
    air_datetime: None
    imdb_fields: None
    ad_languages: list[None]
    credit_cuepoints: CreditCuepoints
    partner_id: str | None
    id: str
    title: str
    policy_match: bool
    creator_tensor_app: None
    version: int
    posterarts: list[str]
    updated_at: AwareDatetime
    hero_images: list[str]
    availability_duration: int
    rt_fields: None
    tags: list[str]
    imdb_id: None
    thumbnails: list[str]
    url: str
    detailed_type: str
    availability_ends: None
    is_cdc: bool
    login_reason: str

class Child(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    type: str
    title: str
    children: list[Child1]
    posterarts: list[None]

class ContentModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    partner_id: str | None
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
    is_sequential: bool | None = None
    is_recurring: bool | None = None
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
