from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict

class Subtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    lang: str | Any = Field(default=None, union_mode='left_to_right')
    lang_alpha3: str | Any = Field(default=None, union_mode='left_to_right')
    lang_translation: str | Any = Field(default=None, union_mode='left_to_right')

class TubiFields(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_sourcing: list[str] | Any = Field(default=None, union_mode='left_to_right')

class CreditCuepoints(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    postlude: float | Any = Field(default=None, union_mode='left_to_right')
    prologue: float | Any = Field(default=None, union_mode='left_to_right')
    intro_start: float | Any = Field(default=None, union_mode='left_to_right')
    intro_end: float | Any = Field(default=None, union_mode='left_to_right')
    recap_start: float | Any = Field(default=None, union_mode='left_to_right')
    recap_end: float | Any = Field(default=None, union_mode='left_to_right')
    earlycredits_start: float | Any = Field(default=None, union_mode='left_to_right')
    earlycredits_end: float | Any = Field(default=None, union_mode='left_to_right')
    prelogue: float | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')
    system: str | Any = Field(default=None, union_mode='left_to_right')
    value: str | Any = Field(default=None, union_mode='left_to_right')
    descriptors: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    lang: str | Any = Field(default=None, union_mode='left_to_right')
    display_name: str | Any = Field(default=None, union_mode='left_to_right')

class Manifest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')

class VideoResource(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    codec: str | Any = Field(default=None, union_mode='left_to_right')
    audio_tracks: list[AudioTrack] | Any = Field(default=None, union_mode='left_to_right')
    resolution: str | Any = Field(default=None, union_mode='left_to_right')
    manifest: Manifest | Any = Field(default=None, union_mode='left_to_right')
    titan_version: str | Any = Field(default=None, union_mode='left_to_right')
    ssai_version: str | Any = Field(default=None, union_mode='left_to_right')
    generator_version: str | Any = Field(default=None, union_mode='left_to_right')

class Monetization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cue_points: list[float] | Any = Field(default=None, union_mode='left_to_right')

class Awards(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_16x9: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_422: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_desktop_tablet: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_large_mobile: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_small_mobile: list[str] | Any = Field(default=None, union_mode='left_to_right')
    landscape_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    linear_larger_poster: list[str] | Any = Field(default=None, union_mode='left_to_right')
    posterarts: list[str] | Any = Field(default=None, union_mode='left_to_right')
    title_art: list[str] | Any = Field(default=None, union_mode='left_to_right')

class VideoMetadatum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    codec: str | Any = Field(default=None, union_mode='left_to_right')
    resolution: str | Any = Field(default=None, union_mode='left_to_right')

class VideoPreview(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    uuid: UUID | Any = Field(default=None, union_mode='left_to_right')

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo: list[str] | Any = Field(default=None, union_mode='left_to_right')
    title_art: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class CreatorTensorApp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images1 | Any = Field(default=None, union_mode='left_to_right')

class Images2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backgrounds: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_16x9: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_422: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_desktop_tablet: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_large_mobile: list[str] | Any = Field(default=None, union_mode='left_to_right')
    hero_feature_small_mobile: list[str] | Any = Field(default=None, union_mode='left_to_right')
    landscape_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    linear_larger_poster: list[str] | Any = Field(default=None, union_mode='left_to_right')
    posterarts: list[str] | Any = Field(default=None, union_mode='left_to_right')
    title_art: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class VideoResource1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    codec: str | Any = Field(default=None, union_mode='left_to_right')
    audio_tracks: list[AudioTrack] | Any = Field(default=None, union_mode='left_to_right')
    resolution: str | Any = Field(default=None, union_mode='left_to_right')
    manifest: Manifest | Any = Field(default=None, union_mode='left_to_right')
    titan_version: str | Any = Field(default=None, union_mode='left_to_right')
    ssai_version: str | Any = Field(default=None, union_mode='left_to_right')
    generator_version: str | Any = Field(default=None, union_mode='left_to_right')

class Child1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_number: str | Any = Field(default=None, union_mode='left_to_right')
    internal_tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    version_id: str | Any = Field(default=None, union_mode='left_to_right')
    content_orientation: str | Any = Field(default=None, union_mode='left_to_right')
    awards: Awards | Any = Field(default=None, union_mode='left_to_right')
    player_type: str | Any = Field(default=None, union_mode='left_to_right')
    is_replay: bool | Any = Field(default=None, union_mode='left_to_right')
    canonical_id: str | Any = Field(default=None, union_mode='left_to_right')
    video_preview_url: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    gn_fields: Any | None = None
    lang: str | Any = Field(default=None, union_mode='left_to_right')
    directors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    video_renditions: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    images: Images2 | Any = Field(default=None, union_mode='left_to_right')
    import_id: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    publisher_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    needs_login: bool | Any = Field(default=None, union_mode='left_to_right')
    ratings: list[Rating] | Any = Field(default=None, union_mode='left_to_right')
    availability_starts: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    series_id: str | Any = Field(default=None, union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')
    has_trailer: bool | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    tubi_fields: TubiFields | Any = Field(default=None, union_mode='left_to_right')
    landscape_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    video_previews: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    display_episode_number: str | Any = Field(default=None, union_mode='left_to_right')
    actors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    video_metadata: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    monetization: Monetization | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    trailers: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    video_resources: list[VideoResource1] | Any = Field(default=None, union_mode='left_to_right')
    subtitles: list[Subtitle] | Any = Field(default=None, union_mode='left_to_right')
    gracenote_id: str | Any = Field(default=None, union_mode='left_to_right')
    backgrounds: list[str] | Any = Field(default=None, union_mode='left_to_right')
    has_subtitle: bool | Any = Field(default=None, union_mode='left_to_right')
    air_datetime: Any | None = None
    imdb_fields: Any | None = None
    ad_languages: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    credit_cuepoints: CreditCuepoints | Any = Field(default=None, union_mode='left_to_right')
    partner_id: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    policy_match: bool | Any = Field(default=None, union_mode='left_to_right')
    creator_tensor_app: Any | None = None
    version: int | Any = Field(default=None, union_mode='left_to_right')
    posterarts: list[str] | Any = Field(default=None, union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    hero_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    availability_duration: int | Any = Field(default=None, union_mode='left_to_right')
    rt_fields: Any | None = None
    tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    imdb_id: Any | None = None
    thumbnails: list[str] | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    detailed_type: str | Any = Field(default=None, union_mode='left_to_right')
    availability_ends: Any | None = None
    is_cdc: bool | Any = Field(default=None, union_mode='left_to_right')
    login_reason: str | Any = Field(default=None, union_mode='left_to_right')

class Child(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    children: list[Child1] | Any = Field(default=None, union_mode='left_to_right')
    posterarts: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class ContentModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_fields: Any | None = None
    channel_logo: str | Any = Field(default=None, union_mode='left_to_right')
    landscape_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    subtitles: list[Subtitle] | Any = Field(default=None, union_mode='left_to_right')
    gn_fields: Any | None = None
    gracenote_id: str | Any = Field(default=None, union_mode='left_to_right')
    is_cdc: bool | Any = Field(default=None, union_mode='left_to_right')
    tubi_fields: TubiFields | Any = Field(default=None, union_mode='left_to_right')
    player_type: str | Any = Field(default=None, union_mode='left_to_right')
    credit_cuepoints: CreditCuepoints | Any = Field(default=None, union_mode='left_to_right')
    lang: str | Any = Field(default=None, union_mode='left_to_right')
    has_trailer: bool | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    valid_duration: int | Any = Field(default=None, union_mode='left_to_right')
    ratings: list[Rating] | Any = Field(default=None, union_mode='left_to_right')
    detailed_type: str | Any = Field(default=None, union_mode='left_to_right')
    channel_id: str | Any = Field(default=None, union_mode='left_to_right')
    is_replay: bool | Any = Field(default=None, union_mode='left_to_right')
    channel_name: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnails: list[str] | Any = Field(default=None, union_mode='left_to_right')
    partner_id: str | Any = Field(default=None, union_mode='left_to_right')
    country: str | Any = Field(default=None, union_mode='left_to_right')
    video_resources: list[VideoResource] | Any = Field(default=None, union_mode='left_to_right')
    needs_login: bool | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    channel_logo_long: str | Any = Field(default=None, union_mode='left_to_right')
    monetization: Monetization | Any = Field(default=None, union_mode='left_to_right')
    version_id: str | Any = Field(default=None, union_mode='left_to_right')
    actors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    internal_tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    video_renditions: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    availability_duration: int | Any = Field(default=None, union_mode='left_to_right')
    publisher_id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    canonical_id: str | Any = Field(default=None, union_mode='left_to_right')
    air_datetime: Any | None = None
    channel_logo_short: str | Any = Field(default=None, union_mode='left_to_right')
    posterarts: list[str] | Any = Field(default=None, union_mode='left_to_right')
    trailers: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    availability_ends: Any | None = None
    policy_match: bool | Any = Field(default=None, union_mode='left_to_right')
    login_reason: str | Any = Field(default=None, union_mode='left_to_right')
    directors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    rt_fields: Any | None = None
    updated_at: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    channel_logo_center: str | Any = Field(default=None, union_mode='left_to_right')
    awards: Awards | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    import_id: str | Any = Field(default=None, union_mode='left_to_right')
    ad_languages: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    version: int | Any = Field(default=None, union_mode='left_to_right')
    video_preview_url: str | Any = Field(default=None, union_mode='left_to_right')
    content_orientation: str | Any = Field(default=None, union_mode='left_to_right')
    availability_starts: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    hero_images: list[str] | Any = Field(default=None, union_mode='left_to_right')
    has_subtitle: bool | Any = Field(default=None, union_mode='left_to_right')
    video_metadata: list[VideoMetadatum] | Any = Field(default=None, union_mode='left_to_right')
    tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    imdb_id: str | Any = Field(default=None, union_mode='left_to_right')
    backgrounds: list[str] | Any = Field(default=None, union_mode='left_to_right')
    video_previews: list[VideoPreview] | Any = Field(default=None, union_mode='left_to_right')
    creator_tensor_app: CreatorTensorApp | Any = Field(default=None, union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')
    series_id: str | Any = Field(default=None, union_mode='left_to_right')
    display_episode_number: str | Any = Field(default=None, union_mode='left_to_right')
    episode_number: str | Any = Field(default=None, union_mode='left_to_right')
    is_sequential: bool | Any = Field(default=None, union_mode='left_to_right')
    is_recurring: bool | Any = Field(default=None, union_mode='left_to_right')
    children: list[Child] | Any = Field(default=None, union_mode='left_to_right')
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
