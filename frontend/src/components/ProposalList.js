import React, { useEffect, useState } from 'react';
import TutorialDataService from '../services/ProposalService';

const ProposalList = () => {
  const [proposal, setProposal] = useState([]);
  const [currentTutorial, setCurrentTutorial] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(-1);

  useEffect(() => {
    retrieveProposals();
  }, []);

  const retrieveProposals = () => {
    TutorialDataService.getAllProposal()
      .then((response) => {
        setProposal(response.data);
        console.log(response.data);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  const setActiveProposal = (tutorial, index) => {
    setCurrentTutorial(tutorial);
    setCurrentIndex(index);
    setData({});
  };

  function getFields(fields) {
    let fieldsList = [];
    fields.forEach((field, index) => {
      console.log(field);
      fieldsList.push(
        <label className="form-label" htmlFor={field.name}>
          {field.label}:
        </label>,
      );
      fieldsList.push(
        <input
          className="form-control"
          style={{ marginBottom: '10px' }}
          type={field.field_type}
          id={field.name}
          name={field.name}
          required={field.required}
          onChange={updateData}
          data-field_id={field.id}
        />,
      );
    });
    return <div>{fieldsList}</div>;
  }
  const [data, setData] = useState({});

  const updateData = (e) => {
    setData({
      ...data,
      [e.target.getAttribute('data-field_id')]: e.target.value,
    });
  };
  const submit = (e) => {
    e.preventDefault();
    data['proposal_id'] = currentTutorial.id;
    TutorialDataService.createRequest(data)
      .then((response) => {
        console.log(response.data);
        alert('Proposta enviada');
        setData({});
        window.location.reload();
      })
      .catch((e) => {
        console.log(e);
      });
  };
  return (
    <div className="list row">
      <div className="col-md-5">
        <h4>Propostas</h4>

        <ul className="list-group">
          {proposal &&
            proposal.map((proposal, index) => (
              <li
                style={{ cursor: 'pointer' }}
                className={
                  'list-group-item ' + (index === currentIndex ? 'active' : '')
                }
                onClick={() => setActiveProposal(proposal, index)}
                key={index}
              >
                {proposal.name}
              </li>
            ))}
        </ul>
      </div>
      <div className="col-md-7">
        {currentTutorial ? (
          <form onSubmit={submit}>
            <h4>{currentTutorial.name}</h4>
            {getFields(currentTutorial.fields)}
            <button type="submit" className="btn btn-primary">
              Enviar Solicitação
            </button>
          </form>
        ) : (
          <div>
            <br />
            <p>Selecione uma Proposta</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProposalList;
