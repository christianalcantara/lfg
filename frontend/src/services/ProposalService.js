import http from '../http-common';

const getAllProposal = () => {
  return http.get('/proposal/proposal/');
};

const createRequest = (data) => {
  return http.post('/proposal/loan_application/request/', data);
};

const ProposalService = {
  getAllProposal,
  createRequest,
};

export default ProposalService;
