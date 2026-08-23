from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    lang: str | None = None
    lang_alpha3: str | None = None
    lang_translation: str | None = None

class CreditCuepoints(BaseModel):
    model_config = ConfigDict(extra='ignore')
    postlude: float | None = None
    prologue: float | None = None
    intro_start: float | None = None
    intro_end: float | None = None
    recap_start: float | None = None
    recap_end: float | None = None
    earlycredits_start: float | None = None
    earlycredits_end: float | None = None
    prelogue: float | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    code: str | None = None
    system: str | None = None
    value: str | None = None
    descriptors: list[Any] | None = None

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    lang: str | None = None
    display_name: str | None = None

class Manifest(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    duration: int | None = None

class VideoResource(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    codec: str | None = None
    audio_tracks: list[AudioTrack] | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    titan_version: str | None = None
    ssai_version: str | None = None
    generator_version: str | None = None

class Monetization(BaseModel):
    model_config = ConfigDict(extra='ignore')
    cue_points: list[float] | None = None

class Awards(BaseModel):
    model_config = ConfigDict(extra='ignore')
    items: list[Any] | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
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

class VideoMetadatum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    codec: str | None = None
    resolution: str | None = None

class VideoPreview(BaseModel):
    model_config = ConfigDict(extra='ignore')
    source: str | None = None
    url: str | None = None
    uuid: UUID | None = None

class VideoResource1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    codec: str | None = None
    audio_tracks: list[AudioTrack] | None = None
    resolution: str | None = None
    manifest: Manifest | None = None
    titan_version: str | None = None
    ssai_version: str | None = None
    generator_version: str | None = None

class Child1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    is_cdc: bool | None = None
    directors: list[str] | None = None
    url: str | None = None
    has_trailer: bool | None = None
    air_datetime: Any | None = None
    series_id: str | None = None
    creator_tensor_app: Any | None = None
    tubi_fields: dict[str, Any] | None = None
    detailed_type: str | None = None
    canonical_id: str | None = None
    description: str | None = None
    has_subtitle: bool | None = None
    availability_ends: Any | None = None
    ratings: list[Rating] | None = None
    internal_tags: list[Any] | None = None
    monetization: Monetization | None = None
    video_renditions: list[Any] | None = None
    player_type: str | None = None
    type: str | None = None
    import_id: str | None = None
    imdb_id: Any | None = None
    video_resources: list[VideoResource1] | None = None
    lang: str | None = None
    gracenote_id: str | None = None
    trailers: list[Any] | None = None
    country: str | None = None
    posterarts: list[str] | None = None
    video_metadata: list[Any] | None = None
    needs_login: bool | None = None
    video_previews: list[Any] | None = None
    content_orientation: str | None = None
    partner_id: Any | None = None
    publisher_id: UUID | None = None
    is_replay: bool | None = None
    policy_match: bool | None = None
    landscape_images: list[str] | None = None
    episode_number: str | None = None
    availability_duration: int | None = None
    hero_images: list[str] | None = None
    images: Images | None = None
    id: str | None = None
    updated_at: AwareDatetime | None = None
    credit_cuepoints: CreditCuepoints | None = None
    ad_languages: list[Any] | None = None
    imdb_fields: Any | None = None
    year: int | None = None
    duration: int | None = None
    version: int | None = None
    backgrounds: list[str] | None = None
    actors: list[str] | None = None
    rt_fields: Any | None = None
    login_reason: str | None = None
    subtitles: list[Any] | None = None
    version_id: str | None = None
    availability_starts: AwareDatetime | None = None
    thumbnails: list[str] | None = None
    awards: Awards | None = None
    tags: list[str] | None = None
    gn_fields: Any | None = None
    display_episode_number: str | None = None
    title: str | None = None
    video_preview_url: str | None = None

class Child(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    type: str | None = None
    title: str | None = None
    children: list[Child1] | None = None
    posterarts: list[Any] | None = None

class ContentModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    imdb_fields: Any | None = None
    channel_logo: str | None = None
    landscape_images: list[str] | None = None
    url: str | None = None
    subtitles: list[Subtitle] | None = None
    gn_fields: Any | None = None
    gracenote_id: str | None = None
    is_cdc: bool | None = None
    tubi_fields: dict[str, Any] | None = None
    player_type: str | None = None
    credit_cuepoints: CreditCuepoints | None = None
    lang: str | None = None
    has_trailer: bool | None = None
    description: str | None = None
    valid_duration: int | None = None
    ratings: list[Rating] | None = None
    detailed_type: str | None = None
    channel_id: str | None = None
    is_replay: bool | None = None
    channel_name: str | None = None
    thumbnails: list[str] | None = None
    partner_id: Any | None = None
    country: str | None = None
    video_resources: list[VideoResource] | None = None
    needs_login: bool | None = None
    type: str | None = None
    channel_logo_long: str | None = None
    monetization: Monetization | None = None
    version_id: str | None = None
    actors: list[str] | None = None
    internal_tags: list[Any] | None = None
    video_renditions: list[Any] | None = None
    availability_duration: int | None = None
    publisher_id: UUID | str | None = Field(default=None, union_mode='left_to_right')
    canonical_id: str | None = None
    air_datetime: Any | None = None
    channel_logo_short: str | None = None
    posterarts: list[str] | None = None
    trailers: list[Any] | None = None
    availability_ends: Any | None = None
    policy_match: bool | None = None
    login_reason: str | None = None
    directors: list[str] | None = None
    rt_fields: Any | None = None
    updated_at: AwareDatetime | None = None
    id: str | None = None
    channel_logo_center: str | None = None
    awards: Awards | None = None
    title: str | None = None
    import_id: str | None = None
    ad_languages: list[Any] | None = None
    duration: int | None = None
    version: int | None = None
    video_preview_url: str | None = None
    content_orientation: str | None = None
    availability_starts: Any | AwareDatetime | None = None
    images: Images | None = None
    hero_images: list[str] | None = None
    has_subtitle: bool | None = None
    video_metadata: list[VideoMetadatum] | None = None
    tags: list[str] | None = None
    imdb_id: str | None = None
    backgrounds: list[str] | None = None
    video_previews: list[VideoPreview] | None = None
    creator_tensor_app: Any | None = None
    year: int | None = None
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
