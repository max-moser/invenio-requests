// This file is part of InvenioRequests
// Copyright (C) 2022 CERN.
//
// Invenio RDM Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import { connect } from "react-redux";
import { getTimelineWithRefresh, timelineStopRefresh } from "./state/actions";
import TimelineFeedComponent from "./TimelineFeed";

const mapDispatchToProps = (dispatch) => ({
  getTimelineWithRefresh: () => dispatch(getTimelineWithRefresh()),
  timelineStopRefresh: () => dispatch(timelineStopRefresh()),
});

const mapStateToProps = (state) => ({
  loading: state.timeline.loading,
  refreshing: state.timeline.refreshing,
  timeline: state.timeline.data,
  error: state.timeline.error,
  isSubmitting: state.timelineCommentEditor.isLoading,
});

export const Timeline = connect(
  mapStateToProps,
  mapDispatchToProps
)(TimelineFeedComponent);